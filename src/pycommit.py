# built-in Python Modules
import os
import sys
import time
# external Python Modules
try:
    import requests
    from github import Github
except ImportError as error:
    sys.stdout.write(error)


class py_commit(object):
    def __init__(self):
        self._username = os.getenv('username')
        self._password = os.getenv('pw')
        self._repo_name = 'commit'

    def instance(self, api):
        pass


# user crendentials
username = os.getenv('username')
password = os.getenv('pw')
repo_name = 'commit'
# create api instance
g = Github(username, password=password)
user = g.get_user()
print(user)
for repo in g.get_user().get_repos():
    print(repo.name)


def repo_check(api):
    for repo in api.get_user().get_repos():
        print(repo.name)
        if repo.name == repo_name:
            print('found')
            return True
        else:
            print('dne')
            return False


# establish session to github
# requests.Session()
# create a new private repository named pycommit
# or check to see if repository already exists
repo_check(g)
# if repo_check(g):
#     print(repo_name + 'already exists')
# else:
#     print('creating repo')
#     repo = user.create_repo(repo_name, description='Test', private=True)
# try:
#     repo = user.create_repo(repo_name, description='Test', private=True)
# # if the repo doesnt exist then we create a new repo
# except raise self.__createException:
#     print(e)
