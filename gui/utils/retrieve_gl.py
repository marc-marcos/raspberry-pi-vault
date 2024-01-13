import requests
import os
import subprocess


def get_gl_repos():
    r = requests.get("https://gitlab.com/api/v4/users/10677309/projects")
    # print(r.json()[0]["http_url_to_repo"])
    repos_json = r.json()

    commands = []
    names = []

    for repo in repos_json:
        commands.append([repo["name"], repo["http_url_to_repo"]])
        names.append(repo["name"])

    try:
        os.chdir("../gl_repos/")

    except FileNotFoundError:
        os.mkdir("../gl_repos")
        os.chdir("../gl_repos/")

    for command in commands:
        try:
            if os.path.exists(f"{command[0]}"):
                os.chdir(f"{command[0]}")
                subprocess.run(["git", "pull"])
                os.chdir("..")

            else:
                subprocess.run(["git", "clone", command[1], command[0]])

        except Exception:
            print("There has been some error.")

    r.close()
    return names


if __name__ == "__main__":
    pass
