from keys import bw_key
import requests

url = "http://localhost:8080"


def unlock_vault(password: str):
    data = {"password": password}
    r = requests.post(url + "/unlock", json=data)

    return r.json()["data"]["raw"]


def save_all_passwords(session_token: str):
    r = requests.get(
        url + "/list/object/items", headers={"Authorization": session_token}
    )

    d = r.json()["data"]["data"]
    a = ""

    for item in d:
        try:
            a += f"{item['name']} ----- {item['login']['username']}:{item['login']['password']}\n"

        except KeyError:
            print("Some error")

    return a


def lock_vault():
    requests.post(url + "/lock")


unlock_vault(bw_key)
a = save_all_passwords(bw_key)
lock_vault()

print(a)

with open("../apples.txt", "w") as f:
    f.write(a)
