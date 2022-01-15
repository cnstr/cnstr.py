<img src="https://canister.me/canister.svg" alt="Canister Logo" title="Canister" align="right" height="60"/>

# Canister.py

[![License](https://img.shields.io/github/license/cnstr/canister.py)](https://github.com/cnstr/canister.py/blob/main/LICENSE)
[![Stars](https://img.shields.io/github/stars/cnstr/canister.py)](https://github.com/cnstr/canister.py/stargazers)
[![LoC](https://img.shields.io/tokei/lines/github/cnstr/canister.py)](https://github.com/cnstr/canister.py)

The official library for interacting with [Canister](https://canister.me) in Python.  
Made with love by [Jaidan](https://github.com/ja1dan).

## 💻 Documentation
See [here](./DOCUMENTATION.md) for all Canister.py documentation.

## ❓ Contributing
See [here](./CONTRIBUTING.md) for instructions on how to contribute.

## ⚡️ Example Usage
Below is a good example of how to use Canister.py.
```py
# import asyncio
import asyncio
# import types
from typing import List
# import canister
from canisterpy import (
    Canister, Package, PackageSearchFields
)

# set up client
client = Canister(user_agent='Canister.py Example')

# main function
async def main(package: str) -> List[Package]:
    # create search fields
    fields = PackageSearchFields()
    # pick out fields
    # we want to search by name and author, so
    fields.set('name', True).set('author', True)
    # search for query
    packages = client.search_package(package, fields)
    # return what we found
    return packages

print(asyncio.run(main('test')))
if not client.is_closed(): client.close()
```