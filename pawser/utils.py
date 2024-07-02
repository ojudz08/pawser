import os, sys
from functools import wraps

def get_initial_directory():
    """ Returns the initial directory of the current working directory"""
    return os.path.abspath(os.path.dirname(sys.argv[0]))


def init_dir(func):
    original_init = func.__init__

    @wraps(original_init)
    def wrapper_initdir(self, *args, **kwargs):
        self.initial_directory = get_initial_directory()
        original_init(self, *args, **kwargs)

    func.__init__ = wrapper_initdir
    return func
