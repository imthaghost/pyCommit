"""pyCommit
"""
__maintainer__ = 'Gary Frederick'
__license__ = 'MIT'
__version__ = '1.0.0'

# built-in Python Modules
from datetime import datetime, timedelta
from threading import Timer
import time
import sys
import os

# local Python Modules
from creds import *
from art import *

# external Python Modules
try:
    import requests
    from github import Github
except ImportError as error:
    sys.stdout.write(str(error))


class pyCommit(object):
    def __init__(self):
        self._username = _get_username()
        self._password = _get_password()
        self._repo_name = 'commit'

    def instance(self, api):
        pass

    def commit(self):
        pass

    def status(self):
        pass

    def push(self):
        pass

    def remote(self):
        pass

    def run(self):
        pass

    def _repo_check(self, api):
        found = None
        for repo in api.get_user().get_repos():
            # repos.append(str(repo.name))
            if str(repo.name) == 'commit':
                found = True

                break
            else:
                found = False
        return found

    def _execution_timer(self, function):
        x = datetime.today()
        y = x.replace(day=x.day, hour=1, minute=0, second=0,
                      microsecond=0) + timedelta(days=1)
        delta_t = y-x

        secs = delta_t.total_seconds()
        t = Timer(secs, function)
        t.start()


def repo_check(api):
    found = None
    for repo in api.get_user().get_repos():
        # repos.append(str(repo.name))
        if str(repo.name) == 'commit':
            found = True

            break
        else:
            found = False
    return found


def execution_timer(function):
    x = datetime.today()
    y = x.replace(day=x.day, hour=1, minute=0, second=0,
                  microsecond=0) + timedelta(days=1)
    delta_t = y-x

    secs = delta_t.total_seconds()
    t = Timer(secs, function)
    t.start()


if __name__ == "__main__":
    username = os.getenv('username')
    password = os.getenv('pw')
    repo_name = 'commit'
    # create api instance
    g = Github(username, password=password)
    user = g.get_user()
    print(user)
    found = repo_check(g)
    if found:
        # we ask the user for the other items
        # the user wants 15 commits a day
        repo = user.get_repo(repo_name)
        content = 'some shit'
        # file creation
        repo.create_file('test.txt', 'init', content)
    else:
        # we tell the user we are creating a new private repository where all of the commits will be held
        try:
            repo = user.create_repo(
                repo_name, description='Pycommit commit repo', private=True)
        except createException:
            #     print(e)
            repo.create_file('test.txt', 'init', 'initial')
