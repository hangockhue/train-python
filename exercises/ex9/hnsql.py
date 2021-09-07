"""
Sample output:

1 Announcing SQL Server on Linux(https://blogs.microsoft.com/blog/2016/03/07/announcing-sql-server-on-linux/)
2 Medium-hard SQL interview questions(https://quip.com/2gwZArKuWk7W)
3 You probably don't need AI/ML. You can make do with well written SQL scripts(https://threadreaderapp.com/thread/987602838594445312.html)
4 SQL queries don't start with SELECT(https://jvns.ca/blog/2019/10/03/sql-queries-don-t-start-with-select/)
5 SQL Murder Mystery(https://mystery.knightlab.com/)
6 SQL: One of the most valuable skills(http://www.craigkerstiens.com/2019/02/12/sql-most-valuable-skill/)
7 How SQL Database Engines Work, by the Creator of SQLite (2008) [video](https://www.youtube.com/watch?v=Z_cX3bzkExE)
8 DuckDB – An embeddable SQL database like SQLite, but supports Postgres features(https://duckdb.org/)
9 What ORMs have taught me: just learn SQL (2014)(https://wozniak.ca/blog/2014/08/03/What-ORMs-have-taught-me-just-learn-SQL/)
10 Google Cloud SQL for Postgres(https://cloud.google.com/sql/docs/postgres/)
11 Dolt is Git for Data: a SQL database that you can fork, clone, branch, merge(https://github.com/dolthub/dolt#dolt)
12 Show HN: Select Star SQL, an interactive SQL book(http://selectstarsql.com)
13 TextQL: Execute SQL Against CSV or TSV(https://github.com/dinedal/textql)
14 How to contact Google SRE by dropping a shell in Cloud SQL(https://offensi.com/2020/08/18/how-to-contact-google-sre-dropping-a-shell-in-cloud-sql/)
15 We Can Do Better Than SQL(https://edgedb.com/blog/we-can-do-better-than-sql)
16 Falcon is a free, open-source SQL editor with inline data visualization(https://github.com/plotly/falcon)
17 SQL is 43 years old – Here’s why we still use it today(http://blog.sqlizer.io/posts/sql-43/)
18 Mastery with SQL: Learn Modern SQL with Postgres(https://www.masterywithsql.com/)
19 Show HN: SQL Police Department – Learn SQL while solving crimes(https://sqlpd.com)
20 What ORMs have taught me: just learn SQL (2014)(http://woz.posthaven.com/what-orms-have-taught-me-just-learn-sql)
21 Show HN: Visual SQL(https://chartio.com/blog/why-we-made-sql-visual-and-how-we-finally-did-it/)
22 Simple Anomaly Detection Using Plain SQL(https://hakibenita.com/sql-anomaly-detection)
23 Show HN: ESQLate – Build minimum viable admin panels with just SQL(https://github.com/forbesmyester/esqlate)
24 SQL Notebook(https://sqlnotebook.com/)
25 Ask HN: What is the best online resource to learn advanced SQL?
26 Modern SQL in PostgreSQL(http://www.slideshare.net/MarkusWinand/modern-sql)
27 Advanced SQL and database books and resources(https://www.neilwithdata.com/advanced-sql)
28 Learn SQL Interactively on Khan Academy(http://cs-blog.khanacademy.org/2015/05/just-released-full-introductory-sql.html)
29 SQL Keys in Depth(https://begriffs.com/posts/2018-01-01-sql-keys-in-depth.html)
30 Writing a SQL database from scratch in Go(https://notes.eatonphil.com/database-basics.html)
"""  # noqa
import time

import requests_html

s = requests_html.HTMLSession()

resp = s.get("https://hn.algolia.com/?q=sql")

time.sleep(1)
resp.html.render()
time.sleep(1)
print(len(resp.html.html), " chars")
with open("hnsql.html", "wt") as f:
    f.write(resp.html.html)

print("Wrote to hnsql.html for debug purpose")

for idx, i in enumerate(
    resp.html.xpath('//div[@class="Story_title"]'), start=1
):
    print(idx, i.text)
