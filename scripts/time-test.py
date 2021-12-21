# time-test.py
# test the time it takes to initialize the Canister object, search for some things, then exit

# import the module that we use to get the time
from datetime import datetime
# start the timer
start = datetime.now()

# import Canister
from canisterpy import Canister

# initialize a Canister object
c = Canister('canister.py testing (0.9)')

# log 100 packages
print('------- PACKAGES -------')
packages = c.search_package('ae', limit=100)
for package in packages:
    print(f'Got {package.identifier} by {package.maintainer} (hosted by {package.repository.get("name")}) on version {package.version}')
print(f'Found {len(packages)} repos in total.')


# log a whole bunch of repos
print ('------- REPOSITORIES ------')
repos = c.search_repo('')
for package in c.search_repo(''):
    print(f'Got {package.name} ({package.uri}) on version {package.version}')
print(f'Found {len(repos)} repos in total.')


# log the time difference
print(f'------- FINISHED in {(datetime.now().timestamp() - start.timestamp()) * 1000} ms. -------')