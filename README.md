# cnstr.py
[![Downloads](https://img.shields.io/pypi/dm/cnstr)](https://pypi.org/project/cnstr/)
[![License](https://img.shields.io/github/license/cnstr/canister.py)](https://github.com/cnstr/cnstr.py/blob/main/LICENSE)

The official library to interact with the Canister API in Python!<br>
For more information about Canister, see our [website](https://canister.me/) and [documentation](https://docs.canister.me/)<br>

### Installation
The library is available to install as a wheel from [PyPi](https://pypi.org/project/cnstr/).<br>
Install it by running `pip install cnstr`<br>

### Documentation
See [here](./DOCUMENTATION.md) for all cnstr.py documentation.

### Example Usage
Below is a good example of how to use cnstr.py.
```py
# import asyncio
import asyncio
# import types
from typing import List
# import canister
from canisterpy import (
	Canister, Package, PackageSearchFields
)

# set up client (user agent is always required so that we may monitor api calls)
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

### Contributing
See [here](./CONTRIBUTING.md) for instructions on how to contribute.
