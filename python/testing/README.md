# Introduction to Testing

## Example Code

See [activation_function_sigmoid.py](activation_function_sigmoid.py).
This snippet is taken from an example in Phase 2.
Recall that it squashes a value into a range 0..1 with a s-shaped curve.

- Is the function implemented correctly?
- How would we know if there was an error in the code?
- If the code is correct today, how might errors be introduced in the future?

## Simple tests with the Python `assert` statement

The `assert` statement [docs](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
allows us to assert something in our code and check it is correct when the code runs.

See [activation_function_sigmoid_asserts.py](activation_function_sigmoid_asserts.py).
Run with `pipenv run python python/testing/activation_function_sigmoid_asserts.py`

- can you write an assertion to check that 1 is equal to 1?
- can you write an assertion to check that 1 is not equal to 2?
- can you write an assertion to check that 1 is less than 2?
- can you write an assertion to check that `random.random()` produces a number between 0 and 1?
    - how might you assert that `random.random()` **always** produces a number between 0 and 1?
- what limitations do you see with assertions like this?

## Notebook-style example

In [sklearn_linreg_example.py](sklearn_linreg_example.py) we have a notebook-like example.

- can you tell if the code is correct?
- try un-commenting the assertion. Can you tell now?

## More capable testing with doctest

Python's built-in [doctest](https://docs.python.org/3/library/doctest.html) module gives us
more advanced testing capabilities than simple assert statements.

See [activation_function_sigmoid_doctest.py](activation_function_sigmoid_doctest.py).
Run with `pipenv run python python/testing/activation_function_sigmoid_doctest.py`

- how does doctest improve upon assert statements?
- where might assert statements be better?
- what limitations can you see for doctest and asserts?

