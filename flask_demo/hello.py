import subprocess

import requests
from flask import Flask
from flask import render_template


app = Flask(__name__)
url = 'https://api.github.com/repos/awesome-jobs/jobs/issues'
app.debug = True


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/about")
def about():
    return """<html><head><title>About
</title></head><h1>This is about page</h1>
</html>"""


def get_processes():
    processes = subprocess.check_output('ps xau'.split())
    return processes.splitlines()


@app.route("/processes")
def processes():
    ps = get_processes()
    return render_template('ps.html', processes=ps)


@app.route('/jobs')
def jobs():
    jobs = []
    res = requests.get(url)
    for j in res.json():
        jobs.append(j['title'])
    return ("<ul>" +
            ''.join(['<li>' + j['title'] + '</li>' for j in res.json()]) +
            "</ul>")


if __name__ == "__main__":
    app.run()
