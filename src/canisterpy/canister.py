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

import urllib

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
        self.__session = session
        self.closed = False
        self.ua = user_agent
        # register closing to happen when deallocated
        register(self.close)
    
    def close(self):
        '''Close and deallocate the current client.'''
        # if the client is closed, tell the user
        if self.closed:
            raise ClosedError('This client is closed.')
        # else close the http session
        if not self.__session.closed:
            run(self.__session.close())
        self.closed = True

    async def search_package(self, query: str, search_fields: SearchFields = SearchFields(), limit: int = 100) -> List[Package]:
        '''Search for a package.
        Args:
            query (str): Query to search for.
            search_fields (Optional[SearchFields]): Fields to search for. (defaults to 'name,author,maintainer,description')
            limit (Optional[str]): Response length limit. (defaults to 100)
        Returns:
            List[Package]: List of packages that Canister found matching the query.
        '''
        if self.closed:
            raise ClosedError('This client is closed.')
        if self.__session is None:
            self.__session = ClientSession()
        # normalize query string
        query = urllib.parse.quote(query)
        # make request
        response = await canister_request(f'/packages/search?query={query}&limit={limit}&searchFields={search_fields.__string__}&responseFields=name,author,maintainer,description&responseFields=identifier,header,tintColor,name,price,description,packageIcon,repository.uri,repository.name,author,maintainer,latestVersion,nativeDepiction,depiction', self.ua, 1, self.__session)
        # convert packages to Package objects
        return [Package(package) for package in response.get('data')]
    
    async def search_repo(self, query: str) -> List[Repo]:
        '''Search for a repo.
        Args:
            query (str): Query to search for.
        Returns:
            List[Repo]: List of repos that Canister found matching the query.
        '''
        if self.closed:
            raise ClosedError('This client is closed.')
        if self.__session is None:
            self.__session = ClientSession()
        # normalize query string
        query = urllib.parse.quote(query)
        # make request
        response = await canister_request(f'/repositories/search?query={query}', self.ua, 1, self.__session)
        # convert packages to Repository objects
        return [Repo(repo) for repo in response.get('data')]

    async def is_repo_piracy(self, query: str) -> bool:
        '''Find out if a repo is piracy.
        Args:
            query (str): Repo URI.
        Returns:
            bool: Whether or not the repo is piracy.
        '''
        if self.closed:
            raise ClosedError('This client is closed.')
        if self.__session is None:
            self.__session = ClientSession()
        # trim url string
        query = query.replace('https://', '').replace('http://', '')
        # get piracy repos
        r = await piracy_repos(self.__session)
        # return
        return query in r