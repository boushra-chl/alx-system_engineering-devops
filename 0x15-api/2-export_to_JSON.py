#!/usr/bin/python3
"""Export data in the CSV format"""

import json
import requests
import sys


def export_to_json(EMPLOYEE_ID):
    """exports data to csv file"""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{EMPLOYEE_ID}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    USERNAME = user_data.get('username')

    todos_url = f'{base_url}/todos/?userId={EMPLOYEE_ID}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    json_data = {
        str(EMPLOYEE_ID): [{"task": todo.get("title"), "completed": todo.get("completed"), "username": todo.get("username"),} for todo in todos_data]}

    json_file = f"{EMPLOYEE_ID}.json"
    with open(json_file, mode="w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <EMPLOYEE_ID>")
    else:
        EMPLOYEE_ID = sys.argv[1]
        export_to_json(EMPLOYEE_ID)
