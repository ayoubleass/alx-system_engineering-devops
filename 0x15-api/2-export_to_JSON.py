#!/usr/bin/python3
"""This script exports data to a json file"""


if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(
        argv[1])
        )
    username = user.json().get("username")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = {}
    tasks = list()
    n = 0
    for task in todos.json():
        if task.get('userId') == int(argv[1]):
            tasks.append(dict(
                task=task.get('title'),
                completed=task.get('completed'),
                username=username
                ))
    data[argv[1]] = tasks
    filename = str(argv[1]) + ".json"
    with open(filename, 'w') as f:
        json.dump(data, f)
