Python typesafety
====

Python typesafety provides a decorator for python functions which uses the normally optional type annotations and performs typechecking based on these annotations both on the function arguments (before function execution) and the return (after function execution).

Non annotated values will not be checked.

Since annotations were only added in python3 this decorator will not work for previous versions of python. Very unfortunate, annotations are awesome. :)
