'''Houses the main class for canister.py.'''
# canister.py

# imports
from .errors import InitializationError, ClosedError
from .requests import canister_request, piracy_repos
from .types import Repo, Package, SearchFields
from aiohttp import ClientSession
from asyncio import run
from atexit import register
from datetime import datetime
from typing import List, Optional
from urllib.parse import quote

class Canister():
    '''The main Canister class.
    Args:
        user_agent (str): User Agent to pass to the Canister API.
        session (Optional[ClientSession]): Optional session to use for requests.
    '''
    def __init__(self, user_agent: str, session: Optional[ClientSession] = None):
        if user_agent is None:
            raise InitializationError('You did not specify a User Agent to use.')
        self.__init_time__ = datetime.now()
        self._session = session
        self._version = 1
        self._ua = user_agent
        self.__closed = False
        # register closing to happen when deallocated
        register(self.close)

    async def __pre_method__(self):
        if self.__closed:
            raise ClosedError('This client is closed.')
        if self._session is None:
            self._session = ClientSession()
    
    def is_closed(self) -> bool:
        '''Checks if the client is closed.'''
        return self.__closed
    
    def close(self):
        '''Close the client.

        No client methods should be running.

        This is idempotent and irreversible.

        No other methods should be called after this one.'''
        # error checks
        if self is None: return
        if self._session is None: return
        # close the http session
        if not self._session.closed:
            run(self._session.close())
        self.__closed = True

    async def search_package(self, query: str, search_fields: SearchFields = SearchFields(), limit: int = 100) -> List[Package]:
        '''Search for a package.
        Args:
            query (str): Query to search for.
            search_fields (Optional[SearchFields]): Fields to search for. (defaults to 'name,author,maintainer,description')
            limit (Optional[str]): Response length limit. (defaults to 100)
        Returns:
            List[Package]: List of packages that Canister found matching the query.
        '''
        # run pre-method function
        await self.__pre_method__()
        # normalize query string
        query = quote(query)
        # make request
        response = await canister_request(f'/packages/search?query={query}&limit={limit}&searchFields={search_fields.__string__}&responseFields=name,author,maintainer,description&responseFields=identifier,header,tintColor,name,price,description,packageIcon,repository.uri,repository.name,author,maintainer,latestVersion,nativeDepiction,depiction', self)
        # convert packages to Package objects
        return [Package(package) for package in response.get('data')]
    
    async def search_repo(self, query: str) -> List[Repo]:
        '''Search for a repo.
        Args:
            query (str): Query to search for.
        Returns:
            List[Repo]: List of repos that Canister found matching the query.
        '''
        # run pre-method function
        await self.__pre_method__()
        # normalize query string
        query = quote(query)
        # make request
        response = await canister_request(f'/repositories/search?query={query}', self)
        # convert packages to Repository objects
        return [Repo(repo) for repo in response.get('data')]

    async def is_repo_piracy(self, query: str) -> bool:
        '''Find out if a repo is piracy.
        Args:
            query (str): Repo URI.
        Returns:
            bool: Whether or not the repo is piracy.
        '''
        # run pre-method function
        await self.__pre_method__()
        # trim url string
        query = query.replace('https://', '').replace('http://', '')
        # get piracy repos
        r = await piracy_repos(self)
        # return
        return query in r