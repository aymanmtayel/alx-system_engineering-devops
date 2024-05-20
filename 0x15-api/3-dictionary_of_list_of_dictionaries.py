#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import json
from requests import get

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    data = get(api + "users").json()

    with open("todo_all_employees.json", "w") as file:
        json.dump({
            user.get("id"): [{"username": user.get("username"),
                              "task": task.get("title"),
                              "completed": task.get("completed")}
                             for task in get(api + "todos",
                                             params={"userId": user.get("id")}
                                             ).json()]
            for user in data}, file)
