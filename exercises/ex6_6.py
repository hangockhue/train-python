#!/usr/bin/env python3

import json
import urllib.request

"""
Read https://docs.python.org/3/howto/urllib2.html#urllib-howto
"""


def repositories(github_login):
    """
    Trả về list name của các repos của GitHub user github_login
    """
    with urllib.request.urlopen(
        "https://api.github.com/users/{}/repos".format(github_login)
    ) as f:
        repos = json.load(f)
    # Sửa function cho phù hợp, trả về kết quả yêu cầu.
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")
    return repos


def solve(input_data):
    return repositories(input_data)


def main():
    for repo_name in solve("pallets"):
        print(repo_name)


if __name__ == "__main__":
    main()
