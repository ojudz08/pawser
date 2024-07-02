import functools
import os, sys


def init_dir(func):
    
    @functools.wraps(func)
    def wrapper_init_dir(*args, **kwargs):
        init_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
        value = func(*args, **kwargs)

        print(f"{func.__name__}() returned {init_dir}")
        return value

    return wrapper_init_dir