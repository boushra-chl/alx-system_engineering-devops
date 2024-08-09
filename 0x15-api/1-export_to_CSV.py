#!/usr/bin/python3
<<<<<<< HEAD
"""export data in CSV format"""

=======
"""Export data in the CSV format"""

import csv
>>>>>>> 180a72d0329eee4e763e5ebf799345b1120e4eab
import requests
import sys


<<<<<<< HEAD
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

=======
def export_to_csv(EMPLOYEE_ID):
    """exports data to csv file"""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{EMPLOYEE_ID}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    USERNAME = user_data.get('username')

    todos_url = f'{base_url}/todos/?userId={EMPLOYEE_ID}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    csv_data = [
            [EMPLOYEE_ID, USERNAME, todo.get("completed"), todo.get("title")]
            for todo in todos_data
    ]

    csv_file = f"{EMPLOYEE_ID}.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(csv_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <EMPLOYEE_ID>")
    else:
        EMPLOYEE_ID = sys.argv[1]
        export_to_csv(EMPLOYEE_ID)
>>>>>>> 180a72d0329eee4e763e5ebf799345b1120e4eab
