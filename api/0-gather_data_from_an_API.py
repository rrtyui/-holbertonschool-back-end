#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API
"""
if __name__ == "__main__":
    import requests
    import sys

    user_id = sys.argv[1]
    url_employee = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(user_id)
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(user_id)
    req_employee = requests.get(url_employee)
    EN = req_employee.json().get('name')
    req_todo = requests.get(url_todo)
    TOTAL_T = len(req_todo.json())
    TASKS = 0
    NUMT = 0
    lists = []
    while TASKS < TOTAL_T:
        if req_todo.json()[TASKS].get('completed') is True:
            lists.append(req_todo.json()[TASKS].get('title'))
            NUMT += 1
        TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format(EN, NUMT, TOTAL_T))
    for t in lists:
        print("\t {}".format(t))
