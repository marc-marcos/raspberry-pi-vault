from github import Github
from github import Auth
from keys import gh_token
import os
import subprocess

auth = Auth.Token(gh_token)

g = Github(auth=auth)

commands = []

for repo in g.get_user().get_repos():
    if len(commands) < 5:
        commands.append(repo.name)

for command in commands:
    try:
        subprocess.run(
            [
                "git",
                "clone",
                f"git@github.com:marc-marcos/{command}.git",
                f"../gh_repos/{command}",
            ]
        )

    except Exception:
        print("Some error")

g.close()
