#!/usr/bin/python3
"""returns information about TODO list progress of an employee"""

import requests
import sys


def get_employee_todo_progress(EMPLOYEE_ID):
    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f'{base_url}/users/{EMPLOYEE_ID}')
    if user_response.status_code != 200:
        print("Failed to retrieve employee information")
        return

    user_data = user_response.json()
    EMPLOYEE_NAME = user_data.get('name')

    todos_response = requests.get(f'{base_url}/todos/?userId={EMPLOYEE_ID}')
    if todos_response.status_code != 200:
        print("Failed to retrieve todos information")
        return

    todos_data = todos_response.json()
    TOTAL_NUMBER_OF_TASKS = len(todos_data)
    list_done_tasks = [task for task in todos_data if task.get('completed')]
    NUMBER_OF_DONE_TASKS = len(list_done_tasks)

    print(f'Employee {EMPLOYEE_NAME} is done with tasks ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})')

    for task in list_done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        EMPLOYEE_ID = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid employee id")
        sys.exit(1)

    get_employee_todo_progress(EMPLOYEE_ID)
