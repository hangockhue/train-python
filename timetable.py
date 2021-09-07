#!/usr/bin/env python
"""
Creates a Trello/GitLab board used as timetable for new course

https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/
Usage: python timetable.py HN2006 2020/06/25
"""
import argparse
import datetime
import os
import logging
import urllib.parse
from typing import Any, List, Tuple

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def create_board(session, board_name):
    print(vars(session))
    board_resp = session.post(
        url="https://api.trello.com/1/boards/", json={"name": board_name},
    )
    board_resp.raise_for_status()
    return board_resp.json()["id"], board_resp.json()["url"]


def create_list(session: Any, board_id: str, name: str = "Thứ 5") -> str:
    resp = session.post(
        "https://api.trello.com/1/boards/{}/lists".format(board_id),
        params={"name": name},
    )
    return resp.json()["id"]


def create_card(session, date, list_id, name) -> None:
    r = session.post(
        "https://api.trello.com/1/cards",
        params={"idList": list_id, "name": name, "due": date},
    )
    r.raise_for_status()


def create_gitlab_board(session, board_name):
    id = urllib.parse.quote_plus("pyfml/prepare")
    resp = session.post(
        url=f"https://gitlab.com/api/v4/projects/{id}/boards",
        json={"name": board_name},
    )
    resp.raise_for_status()
    board_id = resp.json()["id"]
    return board_id, f"https://gitlab.com/pyfml/prepare/-/boards/{board_id}"


def name_to_color(name):
    import hashlib

    md5 = hashlib.md5()
    md5.update(name.encode())
    return "#" + md5.hexdigest()[:6]


def create_gitlab_list(
    session: Any, board_id: str, name: str = "Thứ 5"
) -> str:
    print("creating gitlab list")
    id = urllib.parse.quote_plus("pyfml/prepare")
    label_name = "{}_{}".format(board_id, name)

    def create_project_label():
        resp = session.post(
            url=f"https://gitlab.com/api/v4/projects/{id}/labels",
            json={"name": label_name, "color": name_to_color(label_name)},
        )
        return resp.json()["id"]

    label_id = create_project_label()
    resp = session.post(
        url=f"https://gitlab.com/api/v4/projects/{id}/boards/{board_id}/lists",
        json={"label_id": label_id},
    )
    resp.raise_for_status()

    return label_name


def create_gitlab_card(session, date, list_id, name) -> None:
    """
    This uses list_id but actually a label ID to label the issue.
    GitLab does not care about list in board like Trello.
    """
    label_name = list_id
    print("creating gitlab card", name)
    id = urllib.parse.quote_plus("pyfml/prepare")
    resp = session.post(
        url=f"https://gitlab.com/api/v4/projects/{id}/issues",
        json={"labels": label_name, "due_date": date, "title": name},
    )
    resp.raise_for_status()

    return resp.json()["id"]


def main():
    argp = argparse.ArgumentParser()
    argp.add_argument("course_code", help="e.g: HN2006")
    argp.add_argument("start_date", help="e.g 2020/06/25")
    argp.add_argument(
        "--trello",
        help="Create board on trello instead of GitLab project issue board",
        action="store_true",
    )

    args = argp.parse_args()
    start = datetime.datetime.strptime(args.start_date, "%Y/%m/%d")
    course_code = args.course_code.upper()
    location = "Hà Nội" if course_code.startswith("HN") else "Tp Hồ Chí Minh"

    S = requests.Session()
    if args.trello:
        print("Going to create trello board")
        create_board_fn = create_board
        create_list_fn = create_list
        create_card_fn = create_card
        S.params.update(
            {
                "key": os.environ["TRELLO_KEY"],
                "token": os.environ["TRELLO_TOKEN"],
            }
        )

    else:
        print("Going to create gitlab board")

        def get_gitlab_authen_header():
            token = os.environ["GITLAB_TOKEN"]
            return {"Private-Token": token, "content-type": "application/json"}

        authen_header = get_gitlab_authen_header()
        S.headers.update(authen_header)
        create_board_fn = create_gitlab_board
        create_list_fn = create_gitlab_list
        create_card_fn = create_gitlab_card

    create_timetable(
        create_board_fn,
        create_list_fn,
        create_card_fn,
        S,
        location,
        course_code,
        start,
    )


def create_timetable(
    create_board_fn,
    create_list_fn,
    create_card_fn,
    S,
    location,
    course_code,
    start,
):
    # Create board
    board_name = "Học Python {} PYMI.vn {} timetable".format(
        location, course_code
    )
    logger.info("Creating a new board named %s", board_name)

    board_id, board_url = create_board_fn(S, board_name)

    # List lists
    # resp = S.get(
    #     "https://api.trello.com/1/boards/{}/lists".format(board_id),
    #     params=authen,
    # )
    # resp.json()

    logger.info("Creating two lists, one for Tuesday and other for Thurday")

    list_thursday_id = create_list_fn(S, board_id, name="Thứ 5")
    list_tuesday_id = create_list_fn(S, board_id, name="Thứ 3")

    logger.info("Creating cards for each lesson, add due date")

    def days_for_class(
        start: datetime.datetime, n=12
    ) -> List[Tuple[str, int]]:
        days: List[Tuple[str, int]] = []
        count = 1
        day = start
        while count <= n:
            # tuesday / thursday
            if day.isoweekday() in [2, 4]:
                days.append((day.strftime("%Y/%m/%d"), day.isoweekday()))
                count = count + 1
            day = day + datetime.timedelta(days=1)

        return days

    # TODO fix hardcode 2 & 4, allow user to set which day to learn,
    # not limit to tue/thu
    for idx, (date, dow) in enumerate(days_for_class(start), start=1):
        create_card_fn(
            S,
            date=date,
            list_id=list_thursday_id if dow == 4 else list_tuesday_id,
            name="{} - Bài {}".format(course_code, idx),
        )

    logger.info("Done, URL: %s", board_url)


if __name__ == "__main__":
    main()
