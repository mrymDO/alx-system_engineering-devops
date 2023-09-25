#!/usr/bin/python3
""" gets information about a specific employee's TODO list """

import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

response = requests.get(user_url)
data_user = response.json()
employee_name = data_user.get("name")

response = requests.get(todo_url)
data_todo = response.json()

completed_tasks = [done.get("title")
                   for done in data_todo if done.get("completed") is True]
total_tasks = len(data_todo)

print(f"Employee {employee_name} is done with tasks(
        {len(completed_tasks)}/{total_tasks}): ")
for task in completed_tasks:
    print(f"\t{task}")
