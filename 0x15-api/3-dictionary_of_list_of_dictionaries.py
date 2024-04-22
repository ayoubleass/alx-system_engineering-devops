#!/usr/bin/python3
"""This script"""


if __name__ == "__main__":
    import json
    import requests

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users_info = list()
    for user in users.json():
        user_info = {}
        user_info['id'] = user.get("id")
        user_info['username'] = user.get("username")
        users_info.append(user_info)
    data = {}
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for user in users_info:
        info = list()
        for task in todos.json():
            if task.get("userId") == user['id']:
                temp = dict()
                temp["username"] = user["username"]
                temp["task"] = task["title"]
                temp["completed"] = task["completed"]
                info.append(temp)
        data[str(user["id"])] = info
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
