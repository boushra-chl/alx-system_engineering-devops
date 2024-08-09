#!/usr/bin/python3
"""export data in CSV format"""

import requests
import sys


def get_user_data(EMPLOYEE_ID):
    url = f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Unable to get data for employee ID: {EMPLOYEE_ID}")
        return

    return response.json()

def get_todo_list(EMPLOYEE_ID):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Unable to get data for employee ID: {EMPLOYEE_ID}")
        return

    return response.json()

