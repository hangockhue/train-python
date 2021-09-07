import requests_html

S = requests_html.HTMLSession()

base_url = "https://standardebooks.org"


def get_items(page=1):
    resp = S.get("https://standardebooks.org/ebooks?page={}".format(page))
    return resp.html.xpath("//main/ol/li")


def main():
    page = 1
    counter = 0
    no_author_count = 0
    while True:
        lis = get_items(page)
        if not lis:
            break

        for li in lis:
            try:
                author = li.xpath('//p[@class="author"]/a/span/text()')[0]
            except IndexError:
                author = "Anonymous"
                no_author_count = no_author_count + 1
                if no_author_count > len(lis) / 2:
                    raise Exception(
                        "The author parsing code is broken: {}".format(li.html)
                    )
                else:
                    print("Not found xpath for author:", li)

            title_a = li.xpath("//p[not(@class)]/a")[0]
            title = title_a.xpath("//text()")[0]
            url = title_a.xpath("//@href")[0]
            counter = counter + 1

            print(
                "{} {:<25} - {:<30} - {:<80} ".format(
                    counter, author, title, base_url + url
                )
            )

        page = page + 1


if __name__ == "__main__":
    main()
