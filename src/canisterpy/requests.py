'''Methods for all requests made to the Canister API url.'''
# requests.py

# imports
from aiocache import cached

import aiohttp
import json
from .errors import RequestError

async def canister_request(path: str, ua: str, version: int) -> dict:
    '''Make a request to the Canister API.
    Args:
        path (str): The Canister route to make a request to.
        ua (str): The User Agent to send to the Canister API.
    Returns:
        The request's return value.
    '''
    # initialize try so if anything goes wrong we know about it
    try:
        # set up client
        async with aiohttp.ClientSession() as client:
            # make request
            async with client.get(f'https://api.canister.me/v{version}/community{path}', headers={'User-Agent': ua}) as c:
                # if the status is 200,
                if c.status == 200:
                    # send off our result
                    return json.loads(await c.text())
                # otherwise, crash it
                else:
                    raise RequestError(f'Request to path {path} failed (code {c.status}, v{version}).')
    except:
        raise RequestError(f'Request to path {path} failed.')

@cached(ttl=3600)
async def piracy_repos() -> dict:
    '''Get all piracy repositories.
    Returns:
        The request's return value.
    '''
    # initialize try so if anything goes wrong we know about it
    try:
        # set up client
        async with aiohttp.ClientSession() as client:
            # make request
            async with client.get(f'https://pull.canister.me/piracy-repositories.json') as c:
                # if the status is 200,
                if c.status == 200:
                    # send off our result
                    return json.loads(await c.text())
                # otherwise, crash it
                else:
                    raise RequestError(f'Request to https://pull.canister.me/piracy-repositories.json failed (code {c.status}).')
    except:
        raise RequestError(f'Request to https://pull.canister.me/piracy-repositories.json failed.')