#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv
import csv


if __name__ == "__main__":
    res1 = get('https://jsonplaceholder.typicode.com/todos/')
    todos = res1.json()
    completed = 0
    total = 0
    tasks = []
    res2 = get('https://jsonplaceholder.typicode.com/users')
    users = res2.json()
    for i in users:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')
    
    with open(argv[1] + '.csv', 'w', newline='') as file:
        out = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in todos:
            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.append(i['completed'])
                row.append(i['title'])
                out.writerow(row)
