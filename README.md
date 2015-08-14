# Python typesafety [![Package status](https://img.shields.io/pypi/v/typesafe-hints.svg)](https://pypi.python.org/pypi/typesafe-hints/1.0)

Python typesafety provides a decorator for python functions which uses the normally optional type annotations and perform typechecking based on these annotations both on the function arguments (before function execution) and the return value (after function execution).

Non annotated values will be left untouched.

Since annotations were only added in Python 3 this decorator will not work for previous versions of python. Very unfortunate, annotations are awesome. :)

## Usage

```python
import typesafe

@typesafe
def my_func(this_gets_checked:int, this_doesnt) -> str:
    pass

```

## Overhead

Despite my best attempts at making this decorator as fast and efficient as possible it still introduces a substantial amount of overhead into your program.

However it is designed such that if the python interpreter has been invoked in optimized mode (-O option or PYTHONOPTIMIZE environment variable) the decorator will just return the function itself, posing zero runtime overhead.
