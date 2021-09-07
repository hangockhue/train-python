#!/usr/bin/env python
# coding: utf-8
import datetime
import calendar


def main():
    import argparse

    argp = argparse.ArgumentParser()
    now = datetime.datetime.now()
    argp.add_argument("yyyy", type=int, default=now.year, nargs="?")
    argp.add_argument("mm", type=int, default=now.month, nargs="?")
    argp.add_argument("--no-index", action="store_true")
    args = argp.parse_args()
    yyyy, mm = args.yyyy, args.mm
    print(calendar.month(yyyy, mm))

    start_date = int(input("Pick start date: ").strip())
    start = datetime.date(yyyy, mm, start_date)
    count = 1
    day = start
    # 20 not 12 because sometimes we got holidays/off-days, so prepare for bad
    # cases, otherwise we still can just copy first 12 days
    while count <= 20:
        if day.isoweekday() in (2, 4):
            if not args.no_index:
                print(count, end=" ")
            print(day, day.strftime("%A"))
            count = count + 1
        day = day + datetime.timedelta(days=1)


if __name__ == "__main__":
    main()
