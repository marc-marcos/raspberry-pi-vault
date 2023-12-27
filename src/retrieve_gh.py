from github import Github
from github import Auth
from keys import gh_token
import traceback
import os
import subprocess

auth = Auth.Token(gh_token)

g = Github(auth=auth)

commands = []

for repo in g.get_user().get_repos():
    if len(commands) < 5:
        commands.append(repo.name)

try:
    os.chdir("../gh_repos/")

except FileNotFoundError:
    os.mkdir("../gh_repos/")
    os.chdir("../gh_repos/")

for command in commands:
    try:
        # Antes de hacer esto comprobar si ya existe el directorio
        if os.path.exists(f"{command}"):
            subprocess.run(["git", "pull"])

            print(f"{command} already exists.")

        else:
            subprocess.run(
                [
                    "git",
                    "clone",
                    f"git@github.com:marc-marcos/{command}.git",
                    f"{command}",
                ]
            )

    except Exception:
        print(traceback.format_exc())

g.close()
