import inspect
from functools import partial

__author__ = 'justusadam'


def typesafe(func):
    spec = inspect.getfullargspec(func)
    types = spec.annotations
    def_args = spec.args

    def checkargs(argval):
        for arg, value in argval:
            assert isinstance(value, types.get(arg, object))

    def wrap(*args, **kwargs):

        real_args = filter(lambda v: v not in kwargs, def_args)

        checkargs(zip(real_args, args))
        checkargs(kwargs.items())

        res = func(*args, **kwargs)
        
        checkargs([('return', res)])
        return res

    return wrap
