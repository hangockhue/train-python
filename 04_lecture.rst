4. Git, Tuple, PEP8, ListComps
==============================

Type contructors
----------------

(or converter)

- int
- str
- float
- list
- ...


IO
--

Handling Input and Output.

Read & write file
-----------------

Introduce using file.
open(), modes (r/w/a binary/text), close(), with, iter over lines.

Iterate over lines::

  with open('/etc/hosts') as f:
      for line in f:
          print(line, end='')
  print("Has file f closed? {0}".format(f.closed))


Default encoding depends on OS settings (not always UTF-8).

Tuple unpacking
---------------

- Multi-assignment
- Unpacking in function call with `*`
- When list when tuple?


Any, all
--------

Truthiness
----------

- Given::

  if X:

- What will be `True`? What will be `False`

Identity test
-------------

- Given code::

    x = [1,2,3]
    y = x
    x[0] = 4

  What is y now?

- Use ``id`` to check ID
- Use ``is`` to know if same ID

- ``is`` True/False/None
- ``==`` for everything else
- ``x = range(4); y = x; x is y``
- ``id()``

Tuple
-----

- Immutable
- When list, when tuple
- Unpacking
- Unpacking in function call with `*`::

  def add(a, b):
      return a+ b

  T = (6, 9)
  print(add(*T))

List comprehension
------------------

- Create a list of even numbers < 10::

  evens = []
  for i in range(10):
      if i % 2 == 0:
          evens.append(i)

- Do this shorter::

  evens = [i for i in range(10) if i % 2 == 0]

::

    # let's do list comprehension

    squares = [x**2 for x in v]
    # [1, 9, 25, 49, 81]

::

    # list comprehension with condition (optional)
    [x**2 for x in v if x%3 == 0]

::

    [9, 81]

.. figure:: http://python-3-patterns-idioms-test.readthedocs.org/en/latest/_images/listComprehensions.gif
   :align: center
   :alt:

According to the `python
documentation <https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions>`_,
**a list comprehension consists of square brackets containing an
expression followed by a for clause and zero or more for or if clauses
as shown below:**

::

    [expression for item1 in iterable1 if condition1
                for item2 in iterable2 if condition2
                ...
                for itemN in iterableN if conditionN ]

Mapping
-------

Filtering
---------

Conclude
--------

Use listcomp when you want a list.
Do not abuse.

What is implement?
------------------

pep8/flake8
-----------

https://github.com/pycqa/pycodestyle

Write code to file
------------------

- Write code to file filename.py using an editor::

    Ubuntu: gedit
    Windows: VSCode / Notepad++
    OSX: sublime text

- Run::

  python3 filename.py

- Windows::

  python filename.py

Git basic
---------

- Git is an VCS (version control system).
- There are many VCS (SVN, Mercurial, CVS) but git is the most popular nowaday.

Why use VCS
-----------

- save history/diary of code changes
- sharing code with multiple developers
- everyone changes a code base at the same time
- reverse back to old day
- ...

Why Git, not other VCS?
-----------------------

Who uses git? see bottom of https://git-scm.com/

GitHub vs GitLab
----------------

- Same same but different
- GitLab offers free private repos

Git concept
-----------

- Repository
- Branch
- Commit
