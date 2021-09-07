"""
List all available Python jobs on itviec.com

An example that uses LXML lib with XPATH to extract components from
HTML site.
"""
import datetime
import json

import lxml.etree
import requests


def get_page_tree(page=1):
    resp = requests.get(
        "https://itviec.com/it-jobs/python?page={}".format(page)
    )
    return lxml.etree.HTML(resp.text)


def extract_address(jobnode):
    addresses = []
    for i in jobnode.xpath('.//div[@class="address"]'):
        children = i.getchildren()
        for k in children:
            if k.text:
                addresses.append(k.text.strip())

    return " - ".join(addresses)


def extract_distance_time(jobnode):
    return jobnode.xpath('.//span[contains(@class, "distance-time")]')[
        0
    ].text.strip()


def get_jobs():
    page = 1
    jobs = []
    while True:
        root = get_page_tree(page)
        # if a page not contains this class, there is no job
        # we reached last page
        if not root.xpath('//div[@class="job__body"]'):
            break

        for j in root.xpath('//div[@class="job_content"]'):
            job = j.xpath(".//h2/a")[0]

            path = job.xpath("@href")[0]
            fullurl = "https://itviec.com{}".format(path)
            jobinfo = {
                "title": job.text,
                "url": fullurl,
                "address": extract_address(j),
                "distance_time": extract_distance_time(j),
            }
            jobs.append(jobinfo)
        page = page + 1
    return jobs


def main():
    import argparse

    argp = argparse.ArgumentParser()
    argp.add_argument("-l", "--location", choices=["HN", "HCM"], type=str)
    args = argp.parse_args()

    jobs = get_jobs()
    today = datetime.date.today().strftime("%Y%m%d")
    with open("{}_all_itviec_jobs.json".format(today), "wt") as f:
        json.dump(jobs, f)

    if args.location == "HN":
        location_filter = "Ha Noi"
    elif args.location == "HCM":
        location_filter = "Ho Chi Minh"
    else:
        location_filter = ""

    jobs = (j for j in jobs if location_filter in j["address"])
    for idx, job in enumerate(jobs, start=1):
        print(
            "{idx:>2}. {distance_time:<12} | {address:<25} | {title:<50} | {url:<40}".format(  # noqa
                idx=idx, **job
            )
        )


if __name__ == "__main__":
    main()
