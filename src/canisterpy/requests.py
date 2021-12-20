'''Methods for all requests made to the Canister API url.'''
# requests.py

# imports
from .errors import RequestError
import aiohttp
import json


async def canister_request(path: str, ua: str) -> dict:
    '''Make a request to the Canister API.
    Args:
        path (str): The Canister route to make a request to.
    Returns:
        The request's return value.
    '''
    try:
        async with aiohttp.ClientSession() as client:
            async with client.get(f'https://api.canister.me/v1/community{path}', headers={'User-Agent': ua}) as c:
                if c.status == 200:
                    return json.loads(await c.text())
                else:
                    raise RequestError(f'Request to path {path} failed (code {c.status}).')
    except:
        raise RequestError(f'Request to path {path} failed.')