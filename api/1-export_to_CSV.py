#!/usr/bin/python3
"""
Module 1-export_to_CSV
"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":

    res = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId={}".format(argv[1])
    )
    tsks = json.loads(res.text)
    usrs = requests.get("https://jsonplaceholder.typicode.com/users")
    us = json.loads(usrs.text)
    res_us = {}
    counter = 0
    csv_row = []
    nid = int(argv[1])

    for line in us:
        counter += 1
        res_us.update(line)
        if counter == nid:
            break
    name_us = res_us["username"]

    my_tsks = [
        (i["completed"], i["title"]) for i in tsks
        if "completed" or "title" in i
    ]

    with open('{}.csv'.format(nid), 'w') as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_ALL)
        writer.writerow(csv_row)
        for i, j in my_tsks:
            if i is True:
                csv_row.append("{}".format(nid))
                csv_row.append("{}".format(name_us))
                csv_row.append("True")
                csv_row.append("{}".format(j))
                writer.writerow(csv_row)
                csv_row = []
            else:
                csv_row.append("{}".format(nid))
                csv_row.append("{}".format(name_us))
                csv_row.append("False")
                csv_row.append("{}".format(j))
                writer.writerow(csv_row)
                csv_row = []
