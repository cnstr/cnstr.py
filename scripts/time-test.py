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
for package in c.search_package('ae', limit=100):
    print(f'Got {package.identifier} by {package.maintainer} (hosted by {package.repository.get("name")}) on version {package.version}')

# log 4 repos
print ('------- REPOSITORIES ------')
for package in c.search_repo('pack'):
    print(f'Got {package.name} ({package.uri}) on version {package.version}')

# log the time difference
print(f'------- FINISHED in {(datetime.now().timestamp() - start.timestamp()) * 1000} ms. -------')