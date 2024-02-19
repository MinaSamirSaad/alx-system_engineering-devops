#!/usr/bin/python3
"""
Requests an API with a given employee ID
Returns information about the employee's TODO list in JSON format
"""

if __name__ == "__main__":
    import json
    from requests import get

    tasksURL = 'https://jsonplaceholder.typicode.com/todos/'
    userURL = 'https://jsonplaceholder.typicode.com/users/'
    tasks = get(tasksURL, timeout=5)
    tasks = tasks.json()
    users = get(userURL, timeout=5)
    users = users.json()
    data = {}
    for user in users:
        data[user.get('id')] = []
        for task in tasks:
            if task.get('userId') == user.get('id'):
                data[user.get('id')].append({"username": user.get('username'),
                                             "task": task.get('title'),
                                             "completed": task.get('completed')
                                             })
    with open("todo_all_employees.json", 'w', encoding='utf-8') as jsonFile:
        json.dump(data, jsonFile)
