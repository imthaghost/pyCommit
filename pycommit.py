import os
from github import Github

# user crendentials
username = os.getenv('username')
password = os.getenv('pw')

g = Github(username, password=password)
# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
