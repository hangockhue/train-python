12. System and Network
======================

Lessons and conclusions
-----------------------

- Python builtin types, mutable, immutable
- List for iterating, tuple for unpacking
- Iterate over list
- Iterate over dict
- Iterate over dict, want value
- Dict or list? depends on usage
- Check membership in dict vs in list

- https://wiki.python.org/moin/PythonSpeed

Duck typing
~~~~~~~~~~~

Monkey Patch
------------

algorithm time complexity
-------------------------

- Comparing O(N), O(N^2), O(lg(N)), O(N!)

os
--

Use `os.path.join`, do not manually join for portability.

subprocess
----------

- The only/up-to-date way to run external commands (vs command/os.system)
- But using lib is better.
- import shlex

argparse
--------

- much better than sys.argv
- add_argument()
- parse_args()
- nargs
- optional vs position args
- store_true
- help
- default

sysadmin automation
-------------------

https://github.com/NARKOZ/hacker-scripts

logging
-------

itertools
---------

functools
---------

http server - python 3 version
-------------------------------

Run a server::

  python -m http.server
