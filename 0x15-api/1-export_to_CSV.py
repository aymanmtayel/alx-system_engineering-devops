#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import csv
from requests import get
from sys import argv

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    data = get(api + "users/{}".format(argv[1])).json()
    name = data.get("username")
    todo = get(api + "todos", params={"userId": argv[1]}).json()

    with open("{}.csv".format(argv[1]), "w", newline="") as file:
        write = csv.writer(file, quoting=csv.QUOTE_ALL)
        [write.writerow([argv[1], name,
                        task.get("completed"),
                        task.get("title")]) for task in todo]
