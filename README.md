# cnstr.py

[![Downloads](https://img.shields.io/pypi/dm/cnstr)](https://pypi.org/project/cnstr/)
[![License](https://img.shields.io/github/license/cnstr/canister.py)](https://github.com/cnstr/cnstr.py/blob/main/LICENSE)

The official library to interact with the Canister API in Python!<br>
For more information about Canister, see our [website](https://canister.me/) and [documentation](https://docs.canister.me/)

### Installation

The library is available as a wheel from [PyPi](https://pypi.org/project/cnstr/) and can be installed using `pip`

```
pip install -U cnstr
```

### Documentation

See [here](./DOCUMENTATION.md) for all cnstr.py documentation.

### Example Usage

Below is a goood example of how to use `cnstr.py`

```py
# Imports
import asyncio

from canisterpy import (
    Canister,
    Package,
    PackageSearchFields
)
from typing import List

async def main(package: str) -> List[Package]:
    # Setup a client (user agent is always required)
    # so that we're capable of monitoring API calls
    client = Canister(user_agent='Canister.py Example')

    # Create and correctly setup search fields
    fields = PackageSearchFields()
    fields.set('name', True).set('author', True)

    # Search for the given package query
    # then, close the Canister client instance
    packages = await client.search_package(package, fields)
    await client.close()
    
    # Return the results of the Canister query
    return packages
    
print(asyncio.run(main('test')))
```

### Contributing

See [here](./CONTRIBUTING.md) for instructions on how to contribute.
