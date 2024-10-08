#!/usr/bin/python3
""" This script fetch data from RESTApi and displays it to the stdout"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    r = requests.get(url)
    name = r.json().get('name')
    user_id = r.json().get('id')
    r = requests.get("https://jsonplaceholder.typicode.com/todos/")
    tasks_completed = 0
    total_tasks = 0
    titles = []
    for task in r.json():
        if int(user_id) == task.get("userId"):
            total_tasks += 1
            if task.get('completed') is True:
                tasks_completed += 1
                titles.append("\t " + task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        name, tasks_completed, total_tasks)
         )
    print("\n".join(titles))
