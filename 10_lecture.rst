10. API, Flask, Jinja2, DB, ORM, Sphinx
=======================================

Sphinx
------

Make doc from .rst files in this directory.

Static web and dynamic web
--------------------------

Flask
-----

```
# myapp.py
from flask import Flask
app = Flask(__name__)


def index():
    return "Hello"

app.add_url_rule('/', 'index', index)


if __name__ == "__main__":
    app.run(debug=True)
```

- Dev by: `python myapp.py`
- Real production run by: `gunicorn myapp:app`

Components
~~~~~~~~~~

- Routing
- Templating

Exercise: write an endpoint that return list of running process
(ps xau) in JSON format::

  [
    {
      'PID': NUMBER,
      'CPU': PERCENT_CPU,
      'MEM': PERCENT_MEM,
      'CMD': COMMAND,
    },
    {...}
  ]

- Website is HTML page that endpoints return. We will need to return HTML code,
  so write them in .py file? No, we are not PHP, we have a better way.

Jinja2
------

CGI and WSGI
------------

CGI
~~~

A CGI script is invoked by an HTTP server, usually to process user input
submitted through an HTML <FORM> or <ISINDEX> element.

Most often, CGI scripts live in the server’s special cgi-bin directory. The
HTTP server places all sorts of information about the request (such as the
client’s hostname, the requested URL, the query string, and lots of other
goodies) in the script’s shell environment, executes the script, and sends the
script’s output back to the client.

https://docs.python.org/3/library/cgi.html#introduction

WSGI
~~~~

The Web Server Gateway Interface (WSGI) is a standard interface between web
server software and web applications written in Python. Having a standard
interface makes it easy to use an application that supports WSGI with a number
of different web servers.

Only authors of web servers and programming frameworks need to know every
detail and corner case of the WSGI design. You don’t need to understand every
detail of WSGI just to install a WSGI application or to write a web application
using an existing framework.

https://docs.python.org/3/library/wsgiref.html

ORM
---

What is API?
------------

- Application programming interface.
- Endpoints
- Slug
- URL
- URI

TDD
---

- unittest
- BDD
- http://flask.pocoo.org/docs/0.10/testing/
- https://docs.djangoproject.com/en/1.8/topics/testing/


Top packages
------------

- http://pythonwheels.com/
- https://github.com/hvnsweeting/pypitop
