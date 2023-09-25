#!/usr/bin/python3
"""
Export data in the JSON format
"""

import json
import requests


if __name__ == '__main__':
    users_url = 'https://jsonplaceholder.typicode.com/users'

    users_response = requests.get(users_url).json()

    all_data = {}

    for user in users_response:
        user_id = user.get('id')
        username = user.get('username')
        user_url = f"{users_url}/{user_id}"
        user_response = requests.get(user_url).json()

        todo_url = f"{user_url}/todos"

        todos_response = requests.get(todo_url).json()
        all_data[user_id] = []

        for todo in todos_response:
            all_data[user_id].append({
                                  "task": todo.get('title'),
                                  "completed": todo.get('completed'),
                                  "username": username,
                                  })

        with open("todo_all_employees.json", "w") as jsonfile:
            json.dump(all_data, jsonfile)
