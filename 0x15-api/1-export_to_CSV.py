#!/usr/bin/python3
"""This script to export data in the CSV format."""


if __name__ == "__main__":
    import requests
    from sys import argv

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(
        argv[1])
        )
    username = user.json().get("username")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = {}
    n = 0
    for task in todos.json():
        if task.get('userId') == int(argv[1]):
            n += 1
            data["line " + str(n)] = dict(
                completed=task.get('completed'),
                title=task.get('title')
                )
    FILE_NAME = str(argv[1]) + ".csv"
    lines = list()
    for key, values in data.items():
        line = "\"{}\",\"{}\"".format(str(argv[1]), username)
        for k, v in values.items():
            line += ",\"{}\"".format(v)
        lines.append(line)
        with open(FILE_NAME, 'w') as csv_file:
            csv_file.write("\n".join(lines)) 
