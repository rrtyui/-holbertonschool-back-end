#!/usr/bin/python3
"""
Module 2-export_to_JSON
"""
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
    nid = int(argv[1])
    json_dict = {}
    json_dict.setdefault(nid, [])

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

    for i, j in my_tsks:
        if i is True:
            json_dict[nid].append(dict(task=j,
                                       completed=True, username=name_us))
        else:
            json_dict[nid].append(dict(task=j,
                                       completed=False, username=name_us))

    ob_json = json.dumps(json_dict)
    with open("{}.json".format(nid), "w") as fp:
        fp.write(ob_json)
