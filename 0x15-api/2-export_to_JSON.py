#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import json
from requests import get
from sys import argv

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    data = get(api + "users/{}".format(argv[1])).json()
    name = data.get("username")
    todo = get(api + "todos", params={"userId": argv[1]}).json()

    with open("{}.json".format(argv[1]), "w") as file:
        json.dump({argv[1]: [{"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": name} for task in todo]}, file)
