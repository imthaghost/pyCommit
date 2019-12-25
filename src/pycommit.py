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

# external Python Modules
try:
    import requests
    from github import Github
except ImportError as error:
    sys.stdout.write(str(error))


class pyCommit(object):
    def __init__(self, username, password):
        self._default_repo = 'commit'
        self._new_repo = None
        self._api = Github(username, password)

    def update(self, repository_name, num):
        repo = self._api
        contents = repo.get_contents("test.txt", ref="test")
        repo.update_file(contents.path, "more tests",
                         "more tests", contents.sha, branch="test")

    def _repo_check(self, repo_name=None):
        found = None
        for repo in self._api.get_user().get_repos():
            # repos.append(str(repo.name))
            if str(repo.name) == repo_name:
                found = True

                break
            else:
                found = False
        return found

    def _create_repo(self, new_name, status, description='created with pycommit'):
        self._api.get_user().create_repo(
            new_name, description=description, private=status)

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
