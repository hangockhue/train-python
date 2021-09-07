8. stdlib, decorator, generator, debugging
==========================================

Start using editor to code. Always open Ipython to test.

black
-----

`pip install black`

Auto format code - PEP8 compliant

Class (2)
---------

- Single inheritance.
- Using class, presents Undergraduate, and Master students
- Both have some similar attributes and some different

vars
----

Built-in function that display given object attributes.

Try::

  r = requests.get('https://pymi.vn')
  vars(s)

dir
---

- attributes of the given object.
- try with simple class::

  class Foo(): pass

  f = Foo()
  dir(f)

- try and see dir([1,2,3])
- try and see import math, dir(math)
- getattr/hasattr
- isinstance - do NOT compare type

Exception hierarchy
-------------------

exceptions are classes.

https://docs.python.org/3/library/exceptions.html#exception-hierarchy

Glossary
--------

Iterator
--------

An object representing a stream of data.

- Given a list `L = [4, 5, 6]`, get iterator from it by `it = iter(L)`
- Call `next(it)`
- See what happens
- Explain how `for i in iterable` works.

Generator
---------

- A function which returns a generator iterator::

  def gen():
      yield 1
      yield 2
      yield 3
  it = gen()
  next(it)
  next(it)
  next(it)
  next(it)

- range is NOT a generator::

  r = range(3) # if range is generator, r is iterator now
  next(r) --> ?
  it = iter(r) # so r is just like list, we need to convert it to iterator.
  next(it)
  next(it)
  next(it)
  next(it)

- Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).

- Write a function that return list of 5 elements and its corresponding
  generator. What if the list need to return 1 billion elements?
  What will better if we use generator?
- https://docs.python.org/3/glossary.html#term-generator
- Return generator expression::

    return (s for s in students)

BigO
----

https://wiki.python.org/moin/TimeComplexity

Stdlib
------

PYMOTW
------

https://docs.python.org/3/library/
https://docs.python.org/3/howto/
https://pymotw.com/3/py-modindex.html

time
----

- sleep()
- time()
- while True / time.sleep best practice

pdb
---

The python debugger https://docs.python.org/3/library/pdb.html ::

  python3 -m pdb myscript.py


- When script *doesn't run*, what to do?
- ``python -m pdb /path/script.py -t option``

random
------

- random.randrange
- random.randint
- randon.choice
- random.shuffle

https://docs.python.org/2/faq/library.html#mathematics-and-numerics

datetime
--------

- calculate timedelta.
  How many days are there from 2016/Feb/09 to 2017/Mar/18?
  How many seconds?  http://www.familug.org/2014/08/python-time-delta-in-seconds.html
- format and parse time object.
  Given string d = '02/18/17', get the 69th days after. What is that day?
  datetime.datetime.strptime and datetime.datetime.strftime

timeit
------

Use with ipython %timeit::

  In [2]: %timeit 'x = range(1000,1); sorted(x)'
  The slowest run took 381.51 times longer than the fastest. This could mean that an intermediate result is being cached
  100000000 loops, best of 3: 13.1 ns per loop


itertools
---------

- Over multiple lists::

  for i in itertools.chain(L1, L2):
       pass

- Over multiple dicts::

  for k in collections.ChainMap({'a': 'hhii'}, {'b':'huhu'}):
      pass


collections
-----------

- Counter
- namedtuple
- defaultdict # see doc
- deque # see doc
- OrderedDict # see doc

logging
-------

- basicConfig
- getLogger(__name__)
- debug/info/warning/error/critical
- do not format log, let logger does that.

copy
----

- Assignment statements do not copy objects.
  They create binding between a target and an object.
- Interface of a module is function signatures, exceptions (all thing exposed).
- Shallow vs deep copy, how does they implemented?
- What are copy methods for list and dict, shallow or deep?
- https://docs.python.org/3/library/copy.html
- E.g: when to not use deep copy
  https://github.com/saltstack/salt/commit/63aa8c686bcb0ebc47eb3fc80ac45001e92320ff

os
--

- os.listdir
- os.getuid
- os.getpid
- os.walk
- os.path.join
- os.path.abspath
- os.path.isfile
- os.path.isdir
- os.path.exists

sys
---

- sys.path
- sys.exit
- sys.argv

yaml
----

- http://www.familug.org/2013/06/yaml-la-gi.html
- often used for config files
- pip install pyyaml, import yaml, yaml.dump, yaml.safe_load

StackOverFlow
-------------

http://stackoverflow.com/questions/tagged/python

Start a new project
-------------------

Start small
^^^^^^^^^^^

- Create dir
- New virtualenv
- Install dependencies, create requirements.txt
- Write main.py

**script**

- a text file (python module) that can run
- chmod::

    ls -l scriptname.py
    chmod a+x scriptname.py
    ls -l scriptname.py

- #!/usr/bin/env python3
- https://docs.python.org/3/faq/library.html#how-do-i-make-a-python-script-executable-on-unix

- Split code out to other modules/package.
- Lint with flake8
- Push to GitHub
- Bonus: setup CI (circle CI)

decorator
---------

A function returning another function.

- functions are object.
- function is callable.
- function which returns other function
- use @ notation
- just syntactic sugar
- check all syntactic sugars: ``+``, ``-``, ``__getitem__``,
  ``__str__``.

Syntactic sugar
---------------

- What is `+`, `-`, `==`?
- What is compare? How `x` can compare to `y`?
- Function call? callable.
- Why we can write len(L)? not len(5) ?
- Why we can write L[3]? not 7[3] ?

Linting
-------

What does ``lint`` mean? -> https://en.wikipedia.org/wiki/Lint\_(software)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    tool that flags suspicious usage in software written in any computer
    language

PyLint:
-------

Install pylint: https://www.pylint.org/#install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sudo apt-get install pylint``

or ``pip install pylint``

usage: `read the docs <https://docs.pylint.org/>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

basic usage: ``pylint /path/to/mymodule.py``
