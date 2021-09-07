#!/usr/bin/env python
# coding: utf-8

"""
hnsotw: HackerNews stories of the week.

Get latest week top curated HackerNews stories from hackernewsletter.
"""

import bs4
import feedparser


def get_latest_week_stories():
    # https://mailchi.mp/hackernewsletter/522
    feedurl = "https://us1.campaign-archive.com/feed?u=faa8eb4ef3a111cef92c4f3d4&id=e505c88a2e"  # noqa

    r = feedparser.parse(feedurl)
    entries = r["entries"]
    latest = entries[0]
    print(latest["title"], latest["published"])
    content = latest["content"][0]

    html = content["value"]

    tree = bs4.BeautifulSoup(html, features="lxml")

    ps = tree.find_all("p")

    stories = []

    for p in ps:
        try:
            link, comment = p.find_all("a")
        except ValueError:
            continue
        if "votes" not in link.attrs.get("title", "").lower():
            continue

        stories.append(
            (
                link.attrs.get("title"),
                link.text,
                comment.attrs["href"].replace("&utm_term=comment", ""),
                link.attrs.get("href")[
                    : link.attrs.get("href").find(
                        "?utm_source=hackernewsletter"
                    )
                ],
            )
        )
    return stories


def main():
    import argparse

    argp = argparse.ArgumentParser()
    argp.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Print out all links instead of top 24 stories by votes",
    )
    args = argp.parse_args()

    links = get_latest_week_stories()
    top_stories = sorted(
        links, key=lambda x: int(x[0].split()[1]), reverse=True
    )

    if args.all:
        links = top_stories
    else:
        links = top_stories[:24]

    for (idx, (score, title, cmt_url, url)) in enumerate(links, start=1):
        _votes, vote, _comments, comment = score.split()
        print(
            "{:>2}. votes:    {:>3} {} {}".format(
                idx,
                vote,
                title,
                url,
            )
        )
        print("    comments: {:>3} - {}".format(comment, cmt_url))


if __name__ == "__main__":
    main()
