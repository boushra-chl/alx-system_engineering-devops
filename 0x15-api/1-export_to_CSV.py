#!/usr/bin/python3
"""Export data in the CSV format"""

import sys
import csv
import requests


def export_to_csv(EMPLOYEE_ID):
    """exports data to csv file"""
    user_url = f'https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    USERNAME = user_data.get('username')

    todos_url = f'https://jsonplaceholder.typicode.com/todos/?userId={EMPLOYEE_ID}'
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
