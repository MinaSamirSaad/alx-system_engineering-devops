#!/usr/bin/python3
'''
A script that gathers employee name completed
tasks and total number of tasks from an API
'''

from sys import argv
import requests


if __name__ == "__main__":
    tasksURL = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    userURL = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    tasks = requests.get(tasksURL, timeout=5)
    tasks = tasks.json()
    user = requests.get(userURL, timeout=5)
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
