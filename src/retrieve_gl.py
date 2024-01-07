from keys import gl_token
import gitlab
import os
import subprocess

gl = gitlab.Gitlab(private_token=gl_token)
gl.auth()

projects = gl.projects.list(owned=True)

my_file = open("output.json", "w")

commands = []

for i in projects:
    commands.append(i.asdict()["ssh_url_to_repo"])

my_file.close()

try:
    os.chdir("../gl_repos/")

except FileNotFoundError:
    os.mkdir("../gl_repos/")
    os.chdir("../gl_repos/")

for command in commands:
    try:
        # Antes de hacer esto comprobar si ya existe el directorio
        if os.path.exists(f"{command.split('/')[-1]}"):
            subprocess.run(["git", "pull"])

            print(f"{command} already exists.")

        else:
            subprocess.run(
                [
                    "git",
                    "clone",
                    command,
                    f"{command.split('/')[-1]}",
                ]
            )

    except Exception:
        pass
