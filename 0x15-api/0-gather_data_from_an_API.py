#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

from requests import get
import json
from sys import argv

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    Id = get(api + "users/{}".format(argv[1])).json()
    todo = get(api + "todos", params={"userId": argv[1]}).json()
    completed = [t.get("title") for t in todo if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        Id.get("name"), len(completed), len(todo)))
    for task in completed:
        print("\t ", task)
