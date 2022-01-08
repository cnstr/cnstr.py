# time-test.py
# test the time it takes to initialize the Canister object, search for some things, then exit

# import the module that we use to get the time
from datetime import datetime
# import the module for top-level async
import asyncio
# start the timer
start = datetime.now()

# import Canister
from canisterpy import Canister

# initialize a Canister object
c = Canister('canister.py testing (1.0)')

# fetch 100 packages
s = datetime.now().timestamp()
packages = asyncio.run(c.search_package('ae', limit=100))
fetchtime_packages = (datetime.now().timestamp() - s) * 1000
time_packages = 0
for package in packages:
    time_packages += package.__time__ * 1000


# fetch a whole bunch of repos
s = datetime.now().timestamp()
repos = asyncio.run(c.search_repo(''))
fetchtime_repos = (datetime.now().timestamp() - s) * 1000
time_repos = 0
for repo in repos:
    time_repos += repo.__time__ * 1000

# times
finish_ms = (fetchtime_repos + fetchtime_packages)
packages_avg = (time_packages / len(packages))
repos_avg = (time_repos / len(repos))
net_time = (finish_ms - (time_packages + time_repos))

# log info
print(f'------- STATS -------\nFound {len(repos)} repositories and {len(packages)} packages in {finish_ms} ms.\n\n------- PACKAGES -------\nTotal packages fetch time: {fetchtime_packages} ms\nTotal class assign time: {time_packages} ms\nClass assign time per package (avg): {packages_avg} ms\n\n------- REPOSITORIES -------\nTotal repositories fetch time: {fetchtime_repos} ms\nTotal class assign time: {time_repos} ms\nClass assign time per package (avg): {repos_avg} ms\n\n------- REQUESTS ------\nTotal networking time: {net_time} ms\nNetworking percentage: {round((net_time / finish_ms) * 100, 2)}%')
