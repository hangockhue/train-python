#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Do statistics on students' Merge Requests for given class_id
# TODO: get MR detail, check build result and get list of correct exercises
# Turn to a website, allow students login using GitLab ID
# Or turn to public site, use Lambda generates beautiful dashboard?
# Data can exported as JSON or CSV
"""
import argparse
import datetime
import time
from collections import namedtuple
import json
import os
import urllib.request
import urllib.parse
import re


def send_get(url, headers, data=None):
    if data:
        assert isinstance(data, dict), "data must be a dict, got {}".format(
            type(data)
        )
        url = "{}?{}".format(url, urllib.parse.urlencode(data))

    with urllib.request.urlopen(
        urllib.request.Request(url, headers=headers)
    ) as response:
        if response.status == 200:
            payload = response.read().decode("utf-8")
            return json.loads(payload)
        else:
            raise Exception("Failed {}".format(payload))


def main():
    argp = argparse.ArgumentParser(__doc__)
    argp.add_argument("class_id", help="E.g pymihcm1804", type=str)

    args = argp.parse_args()
    class_id = args.class_id
    token = open(os.path.expanduser("~/.config/gitlab")).read().strip()
    create_weekly_mr_stats_issue(class_id, token)


def ex_count_by_students(list_mr, base_url, ex_count, headers):
    exes = set()
    for mr in list_mr:
        url = base_url.format(mr)
        print(url)
        try:
            res = send_get(url, headers=headers)
            time.sleep(1)
            changes = res["changes"]
        except Exception as e:
            print(e)
            continue

        for change in changes:
            path = change["old_path"]
            try:
                ex = re.search(r"ex\d{1,2}", path).group()
            except AttributeError:
                ex = ""
            exes.add(ex)
    for ex in exes:
        try:
            ex_count[ex] += 1
        except KeyError:
            pass

    return ex_count


def create_weekly_mr_stats_issue(class_id, token, ping_class=False):
    Student = namedtuple("Student", ["gitlabid", "name", "openMR", "closeMR"])

    gitlab_time_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    start_2018 = datetime.datetime(2018, 1, 1)
    start_2018_str = datetime.datetime.strftime(start_2018, gitlab_time_format)

    headers = {"Private-Token": token, "content-type": "application/json"}

    base_url = "https://gitlab.com/api/v4/"
    group_members = base_url + "groups/{}/members"

    resp_data = send_get(
        group_members.format(class_id), headers=headers, data={"per_page": 100}
    )

    cntr = 1
    students = []
    print("List of {} students".format(class_id))
    for student in resp_data:
        if isinstance(student, str):
            print(student, resp_data)
            continue
        if student["access_level"] < 50:
            s = Student(student["username"], student["name"], 0, 0)
            print(cntr, s)
            students.append(s)
            cntr += 1

    # resp = requests.get('https://gitlab.com/api/v4/projects/pyfml%2Fpyfml',
    #                    headers=headers)
    # resp_data = resp.json()
    # the URL get from above resp
    MR_URL = "https://gitlab.com/api/v4/projects/1591562/merge_requests"

    merge_requests = []
    page = 1
    while True:
        print("Processing MRs page {}".format(page))
        resp = send_get(
            MR_URL,
            headers=headers,
            data={
                "per_page": 100,
                "page": page,
                "created_after": start_2018_str,
            },
        )
        if not resp:
            break
        merge_requests.extend(resp)
        page = page + 1
    print(len(merge_requests))

    counter = {
        s.gitlabid: {"openMR": 0, "closeMR": 0, "totalMR": 0} for s in students
    }

    gitlabids = [s.gitlabid for s in students]

    for mr in merge_requests:
        mr_author = mr["author"]["username"]
        if mr_author not in gitlabids:
            continue

        if mr["state"] == "opened":
            counter[mr_author]["openMR"] += 1
        else:
            counter[mr_author]["closeMR"] += 1
        print(
            mr_author, mr["created_at"], "!{}".format(mr["iid"]), mr["state"]
        )

    username_to_names = {s.gitlabid: s.name for s in students}

    columns = "Rank", "GitLabID", "openMRs", "closeMRs", "Name"
    table_sep = ["---"] * len(columns)

    data = [columns, table_sep]
    for rank, (username, mr_count) in enumerate(
        sorted(counter.items(), key=lambda x: x[1]["openMR"], reverse=True),
        start=1,
    ):

        user_merge_requests = sorted(
            [
                "!{}".format(mr["iid"])
                for mr in merge_requests
                if mr["author"]["username"] == username
            ]
        )
        arow = [
            str(rank),
            username,
            str(mr_count["openMR"]),
            str(mr_count["closeMR"]),
            " ".join([username_to_names[username]] + user_merge_requests),
        ]
        data.append(arow)

    # Counting exercises by finding changes on every mr of every student
    ls_ex = ['ex3', 'ex35', 'ex4', 'ex5', 'ex6', 'ex69', 'ex7', 'ex8']
    ex_count = {ex: 0 for ex in ls_ex}
    base_change_url = ('https://gitlab.com/api/v4/projects/'
                       '1591562/merge_requests/{}/changes')
    for username in gitlabids:
        print(username)
        user_mr = [mr["iid"] for mr in merge_requests
                   if mr["author"]["username"] == username]
        ex_count_by_students(user_mr, base_change_url, ex_count, headers)

    data.append(["---"])
    data.append(["Num", "Exercises", "Count"])
    data.append(["---", "---", "---"])
    for idx, (ex, ex_count) in enumerate(ex_count.items(), start=1):
        data.append([str(idx), ex, str(ex_count)])

    description = "\n".join(["|".join(row) for row in data])
    if ping_class:
        description = description + "\n@{}".format(class_id)

    label = class_id
    ISSUE_URL = "https://gitlab.com/api/v4/projects/1591562/issues"
    json_data = json.dumps(
        {
            "title": "[{}]: bảng tổng soát ngày {}".format(
                label, datetime.datetime.now().strftime("%Y-%m-%d")
            ),
            "description": description,
            # 'labels': ["hcm1804"] - '{"error":"labels is invalid"}'
        }
    ).encode("utf-8")
    with urllib.request.urlopen(
        urllib.request.Request(ISSUE_URL, headers=headers, data=json_data)
    ) as response:
        if response.status == 201:
            payload = response.read().decode("utf-8")
            created_issue = json.loads(payload)
            print("Created {}".format(created_issue["web_url"]))
        else:
            print("Failed {}".format(payload))


def lambda_handler(*args):
    # For run on AWS Lambda
    import base64
    import boto3

    client = boto3.client("kms")
    encrypted_gitlab_token = "AQICAHhTH9iFUXSe2SisnI/nV9WRq6R8Ez2U5kEUMGVej/D3OQGWmi9PgDfzdLTopgwpUhRjAAAAcjBwBgkqhkiG9w0BBwagYzBhAgEAMFwGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMbTM5BHfFwFimHlqaAgEQgC9m27xNr+hEEDLqtsw/4R/l/Z0MBz1hX+owrPknaH8EkuyJl5xm6rKbG1WCvjM2fQ=="  # noqa
    gitlab_token = client.decrypt(
        CiphertextBlob=base64.b64decode(encrypted_gitlab_token)
    )["Plaintext"].decode("ascii")

    class_id = os.environ["class_id"]
    token = gitlab_token
    create_weekly_mr_stats_issue(class_id, token, ping_class=True)


if __name__ == "__main__":
    main()
