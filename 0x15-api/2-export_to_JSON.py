#!/usr/bin/python3
"""
Requests an API with a given employee ID
Returns information about the employee's TODO list in JSON format
"""

if __name__ == "__main__":
    import json
    from requests import get
    from sys import argv

    if len(argv) < 2 or not argv[1].isdigit():
        exit()

    tasksURL = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    userURL = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    tasks = get(tasksURL, timeout=5)
    tasks = tasks.json()
    user = get(userURL, timeout=5)
    user = user.json()
    data = []

    with open(f"{argv[1]}.json", 'w', encoding='utf-8') as jsonFile:
        for task in tasks:
            data.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user.get('username')})
        json.dump({argv[1]: data}, jsonFile)
