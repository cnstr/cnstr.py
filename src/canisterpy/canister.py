'''Houses the main class for canister.py.'''
# canister.py

# imports
from .errors import (
    ClosedError, InitializationError, RequestError
)
from .types import (
    Repo, Package, PackageSearchFields, RepositorySearchFields
)
from aiohttp import ClientSession
from aiocache import cached
from asyncio import run
from atexit import register
from datetime import datetime
from typing import List, Optional
from urllib.parse import quote

import logging

_log = logging.getLogger(__name__)

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
        self.__version = 1
        self.__ua = user_agent
        self.__closed = False
        # register closing to happen when deallocated
        register(self.close)

    async def __pre_method__(self):
        if self.__closed:
            raise ClosedError('This client is closed.')
        if self.__session is None:
            _log.info('Creating new AIOHTTP client.')
            self.__session = ClientSession()

    async def __canister_request(self, path: str) -> dict[str, str]:
        '''Make a request to the Canister API.
        Args:
            path (str): The Canister route to make a request to.
        Returns:
            dict[str, str]: The request's return value.
        '''
        # initialize try so if anything goes wrong we know about it
        try:
            _log.debug('Making request to path %s using Canister version %s.', path, self.__version)
            # make request
            async with self.__session.request(method='GET', url=f'https://api.canister.me/v{self.__version}/community{path}', headers={'User-Agent': self.__ua}) as c:
                # if the status is 200,
                if c.status == 200:
                    # send off our result
                    return (await c.json())
                # otherwise, crash it
                else:
                    raise RequestError(f'Request to path {path} failed (code {c.status}, Canister v{self.__version}).')
        except:
            raise RequestError(f'Request to path {path} failed.')

    @cached(ttl=3600)
    async def __piracy_repos(self) -> list[str]:
        '''Get all piracy repositories.
        Returns:
            list[str]: List of piracy repos.
        '''
        # initialize try so if anything goes wrong we know about it
        try:
            _log.debug('Making routine request to https://pull.canister.me/piracy-repositories.json.')
            # make request
            async with self.__session.request(method='GET', url=f'https://pull.canister.me/piracy-repositories.json') as c:
                # if the status is 200,
                if c.status == 200:
                    # send off our result
                    return (await c.json())
                # otherwise, crash it
                else:
                    raise RequestError(f'Request to https://pull.canister.me/piracy-repositories.json failed (code {c.status}).')
        except:
            raise RequestError(f'Request to https://pull.canister.me/piracy-repositories.json failed.')
    
    def is_closed(self) -> bool:
        '''Check if the client is closed.'''
        return self.__closed
    
    def close(self):
        '''Close the client.

        No client methods should be running.

        This is idempotent and irreversible.

        No other methods should be called after this one.'''
        # error checks
        if self is None: return
        if self.__session is None: return
        # close the http session
        if not self.__session.closed:
            run(self.__session.close())
        self.__closed = True

    async def search_package(self, query: str, search_fields: PackageSearchFields = PackageSearchFields().all_true(), limit: int = 100) -> List[Package]:
        '''Search for a package.
        Args:
            query (str): Query to search for.
            search_fields (Optional[PackageSearchFields]): Fields to search for.
            limit (Optional[str]): Response length limit. (defaults to 100)
        Returns:
            List[Package]: List of packages that Canister found matching the query.
        '''
        # run pre-method function
        await self.__pre_method__()
        # normalize query string
        query = quote(query)
        # make request
        response = await self.__canister_request(f'/packages/search?query={query}&limit={limit}&searchFields={search_fields.__string__}&responseFields=*')
        # convert packages to Package objects
        return [Package(package) for package in response.get('data')]
    
    async def search_repo(self, query: str, search_fields: RepositorySearchFields = RepositorySearchFields().all_true()) -> List[Repo]:
        '''Search for a repo.
        Args:
            query (str): Query to search for.
            search_fields (Optional[PackageSearchFields]): Fields to search for.
        Returns:
            List[Repo]: List of repos that Canister found matching the query.
        '''
        # run pre-method function
        await self.__pre_method__()
        # normalize query string
        query = quote(query)
        # make request
        response = await self.__canister_request(f'/repositories/search?query={query}&searchFields={search_fields.__string__}')
        # convert packages to Repository objects
        return [Repo(repo) for repo in response.get('data')]

    async def is_repo_safe(self, query: str) -> bool:
        '''Find out if a repo is safe.
        Args:
            query (str): Repo URI.
        Returns:
            bool: Whether or not the repo is safe.
        '''
        # run pre-method function
        await self.__pre_method__()
        # trim url string
        query = query.replace('https://', '').replace('http://', '')
        # get piracy repos
        r = await self.__piracy_repos()
        # return
        return query in r