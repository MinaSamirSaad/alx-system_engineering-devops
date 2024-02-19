#!/usr/bin/python3
"""
Requests an API with a given employee ID
Returns information about the employee's TODO list in CSV format
"""

if __name__ == "__main__":
    import csv
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

    with open(f"{argv[1]}.csv", 'w', encoding='utf-8') as csvFile:
        csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            csvWriter.writerow([argv[1], user.get('username'),
                                task.get('completed'), task.get('title')])
