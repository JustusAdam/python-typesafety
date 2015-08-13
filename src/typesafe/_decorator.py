import inspect
import string

__author__ = 'justusadam'


ERROR_MESSAGE = string.Template(
    'Expected type \'$expected\' for argument \'$name\', but got \'$received\'.'
)


def typesafe(func):
    """
    Tests the decorated function on every call to see if the arguments and
    return values line up with any potential type hints given in the function
    signature.

    This decorator will only check for correctness of type if the interpreter
    is run in debug mode (default method of invocation).  If the interpreter was
    invoked invoked in optimised mode (-O option or PYTHONOPTIMIZE specified)
    this decorator will just return the function unchanged, thus creating zero
    runtime overhead.
    """

    spec = inspect.getfullargspec(func)
    types = spec.annotations
    def_args = spec.args

    def checkargs(argval_pairs):
        for arg, value in argval_pairs:
            if not isinstance(value, types.get(arg, object)):
                raise TypeError(
                    ERROR_MESSAGE.substitute(
                        expected=types[arg],
                        received=type(value),
                        name=arg
                    )
                )

    def wrap(*args, **kwargs):

        real_args = filter(lambda v: v not in kwargs, def_args)

        checkargs(zip(real_args, args))
        checkargs(kwargs.items())

        res = func(*args, **kwargs)

        checkargs([('return', res)])
        return res

    if __debug__:
        return wrap
    else:
        return func
