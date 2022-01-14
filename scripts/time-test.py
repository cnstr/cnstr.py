'''test the time it takes to initialize the Canister object, search for some things, then exit'''
# time-test.py

# import the module for loops
import asyncio
# import the module that we use to measure the time
from datetime import datetime
# import name from os
from os import name

# import Canister
from canisterpy import Canister

# initialize a Canister object
c = Canister('canister.py testing (1.0)')

# fix asyncio on windows
if name == 'nt': asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# create a loop
loop = asyncio.new_event_loop()

# fetch 100 packages
s = datetime.now().timestamp()
packages = loop.run_until_complete(c.search_package('test', limit=100))
fetchtime_packages = (datetime.now().timestamp() - s) * 1000
time_packages = 0
for package in packages: time_packages += package.__time__ * 1000

# fetch a whole bunch of repos
s = datetime.now().timestamp()
repos = loop.run_until_complete(c.search_repo(''))
fetchtime_repos = (datetime.now().timestamp() - s) * 1000
time_repos = 0
for repo in repos: time_repos += repo.__time__ * 1000

# close loop
if not loop.is_closed(): loop.close()

# times
finish_ms = (fetchtime_repos + fetchtime_packages)
packages_avg = (time_packages / len(packages))
repos_avg = (time_repos / len(repos))
net_time = (finish_ms - (time_packages + time_repos))

# log info
print(f'------- CANISTER.PY STATS -------\nFound {len(repos)} repositories and {len(packages)} packages in {finish_ms} ms.\n')
print(f'------- PACKAGES -------\nTotal packages fetch time: {fetchtime_packages} ms\nTotal class assign time: {time_packages} ms\nClass assign time per package (avg): {packages_avg} ms\n')
print(f'------- REPOSITORIES -------\nTotal repositories fetch time: {fetchtime_repos} ms\nTotal class assign time: {time_repos} ms\nClass assign time per package (avg): {repos_avg} ms\n')
print(f'------- REQUESTS ------\nTotal networking time: {net_time} ms\nNetworking percentage: {round((net_time / finish_ms) * 100, 2)}%')