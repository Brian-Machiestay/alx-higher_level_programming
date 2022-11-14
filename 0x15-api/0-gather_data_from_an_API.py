#!/usr/bin/python3
"""gather data from an API"""
import requests
from sys import argv
import json

if __name__ == "__main__":
    emp_id = argv[1]
    emp_info = 'https://jsonplaceholder.typicode.com/users/' + emp_id
    all_todos = 'https://jsonplaceholder.typicode.com/todos'
    get_emp_info = json.loads(requests.get(emp_info).text)
    get_all_todos = json.loads(requests.get(all_todos).text)
    to_dos = 0
    todos_done = 0
    todos_done_list = []
    for item in get_all_todos:
        if item['userId'] == int(emp_id):
            to_dos += 1
            if item["completed"] == True:
                todos_done_list.append(item["title"])
                todos_done += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(get_emp_info["name"], todos_done, to_dos))
    for item in todos_done_list:
        print("\t {}".format(item))
