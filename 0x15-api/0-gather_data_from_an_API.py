#!/usr/bin/python3
'''
A script that gathers employee name completed
tasks and total number of tasks from an API
'''

if __name__ == "__main__":
    from sys import argv
    from requests import get

    if len(argv) < 2 or not argv[1].isdigit():
        exit()

    tasksURL = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    userURL = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    tasks = get(tasksURL, timeout=5)
    tasks = tasks.json()
    user = get(userURL, timeout=5)
    user = user.json()

    completed = []
    for task in tasks:
        if task.get('completed') is True:
            completed.append(task.get('title'))

    userName = user.get('name')
    compSize = len(completed)
    print(
        f"Employee {userName} is done with tasks({compSize}/{len(tasks)}):")
    for task in completed:
        print(f"\t {task}")
