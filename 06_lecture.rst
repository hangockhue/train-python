6. File, JSON, Function, Exception
==================================

Name and Object
---------------

- naming
- binding
- id

try/except basic
----------------

::

  d = {'lactroi': 10041243}
  try:
      views = d['lactroi']
  except KeyError as e:
      print(e)
  else:
      print("Đứng đầu bảng xếp hạng là Lạc trôi với %d views" % views)

with statement
--------------

- auto close resources.
- context manager protocol.
  https://docs.python.org/2/whatsnew/2.6.html?highlight=contextmanager#pep-343-the-with-statement

JSON
----

- often used for API
- Dump json::

  $ echo '{"message": "Validation Failed", "errors": [{"field": "title", "code": "missing_field", "resource": "Issue"}]}' | python -m json.tool
  {
      "errors": [
          {
              "code": "missing_field",
              "field": "title",
              "resource": "Issue"
          }
      ],
      "message": "Validation Failed"
  }


CSV
---

Pickle
------

XML
---

User-defined function
---------------------

double = lambda x: x * 2
print(double(2))

sum2 = lambda x, y: x + y

Function
--------

- Built-in functions
- User-defined function::

    def func_name(arg1, args):  # function signature
        '''Docstring
        end of docstring'''

        body_of_function
        return something

::
    def calculate_average_age(first_age, second_age):
        total_of_all_ages = first_age + second_age
        return total_of_all_ages / 2

- Function name, indent
- Return None, return value
- Keyword argument, position argument
- Default argument, position, default value types
- Local variable scope
- Return best practice (one type only)
- When to write a function (need to repeat more than twice)
- Mandatory arguments, optional arguments
- Positional arguments, keyword arguments
- Function aliasing: https://github.com/saltstack/salt/blob/develop/salt/states/virtualenv_mod.py#L274
- Side effect
- Function in function
- Meaning of function which has name starts with ``_``
- ``*args, **kwargs, print(*args)``  # after dict only

Recursive function
^^^^^^^^^^^^^^^^^^
- Factorial::

	def giai_thua(n):
		if n == 0:
			return 1
		return n*giai_thua(n-1)

- Try giai_thua(2000)
- RecursionError: maximum recursion depth exceeded
- Write non-recursive function to calculate factorial.

References
----------

- Exception: https://docs.python.org/3/tutorial/errors.html#handling-exceptions
- With: https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
- JSON: https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json
   http://www.familug.org/2012/09/json-tat-ca-trong-bai-nay.html
- Pickle: https://docs.python.org/3/library/pickle.html
- Function: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Code: https://github.com/familug/FAMILUG/tree/master/Python
- Famous lib code: https://github.com/requests/requests/blob/master/requests/utils.py
- Google Map API: https://developers.google.com/places/web-service/search#PlaceSearchResponses
