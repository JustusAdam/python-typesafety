# Python typesafety [![Package status](https://img.shields.io/pypi/v/typesafe-hints.svg)](https://pypi.python.org/pypi/typesafe-hints/1.0)

Python typesafety provides a decorator for python functions which uses the normally optional type annotations and performs typechecking based on these annotations both on the function arguments (before function execution) and the return (after function execution).

Non annotated values will not be checked.

Since annotations were only added in python3 this decorator will not work for previous versions of python. Very unfortunate, annotations are awesome. :)

# Overhead

Despite my best attempts at making this decorator as fast and efficient as possible it still introduces a substantial amount of overhead into your program.

However it is designed such that if the python interpreter has been invoked in optimized mode (-O option or PYTHONOPTIMIZE environment variable) the decorator will just return the function itself, posing zero runtime overhead.

Ergo as long as your project runs in optimized mode on production you don't have to delete the decorator in production.
