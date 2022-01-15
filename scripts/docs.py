'''Generate documentation for certain Canister.py methods.'''
# docs.py

# imports
import canisterpy as cpy
from inspect import (
    isclass, isfunction, iscoroutinefunction
)

def normalize(tn: str): return tn.replace('        ', '    ')

def doc(td: object):
    if isclass(td):
        print(f'# {td.__name__} (class):  {td.__doc__}')
        for method in [method for method in dir(td) if method.startswith('__') is False]:
            func = getattr(td, method)
            print(f'# {func.__name__} ({"`asynchronous`" if iscoroutinefunction(func) else "`synchronous`"} {type(func).__name__} of {td.__name__}):  {normalize(str(func.__doc__))}')
    elif isfunction(td): print(f'# {td.__name__} ({"`asynchronous`" if iscoroutinefunction(td) else "`synchronous`"} {type(td).__name__}):  {normalize(str(td.__doc__))}')
    else: print(f'# {td.__name__} ({type(td).__name__}):  {str(td.__doc__)}')

for c in cpy.__dict__:
    if not c.startswith('__') and c[0].isupper() and not 'error' in c.lower(): doc(getattr(cpy, c))

exit(0)