'''Methods for all requests made to the Canister API url.'''
# requests.py

# imports
from .errors import RequestError
from aiocache import cached
from aiohttp import ClientSession
from json import loads

async def canister_request(path: str, klass) -> dict:
    '''Make a request to the Canister API.
    Args:
        path (str): The Canister route to make a request to.
        ua (str): The User Agent to send to the Canister API.
    Returns:
        The request's return value.
    '''
    # initialize try so if anything goes wrong we know about it
    try:
        # make request
        async with klass._session.request(method='GET', url=f'https://api.canister.me/v{klass._version}/community{path}', headers={'User-Agent': klass._ua}) as c:
            # if the status is 200,
            if c.status == 200:
                # send off our result
                return loads(await c.text())
            # otherwise, crash it
            else:
                raise RequestError(f'Request to path {path} failed (code {c.status}, v{klass._version}).')
    except:
        raise RequestError(f'Request to path {path} failed.')

@cached(ttl=3600)
async def piracy_repos(klass) -> dict:
    '''Get all piracy repositories.
    Returns:
        The request's return value.
    '''
    # initialize try so if anything goes wrong we know about it
    try:
        # make request
        async with klass._session.request(method='GET', url=f'https://pull.canister.me/piracy-repositories.json') as c:
            # if the status is 200,
            if c.status == 200:
                # send off our result
                return loads(await c.text())
            # otherwise, crash it
            else:
                raise RequestError(f'Request to https://pull.canister.me/piracy-repositories.json failed (code {c.status}).')
    except:
        raise RequestError(f'Request to https://pull.canister.me/piracy-repositories.json failed.')