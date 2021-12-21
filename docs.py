# shitty doc generator

# imports
import canisterpy
import inspect


def doc(td: object):
    bs = "\\"
    if inspect.isclass(td):
        print(f'# {td.__name__} (class):  {td.__doc__}')
        for method in [method for method in dir(td) if method.startswith('__') is False]:
            func = getattr(td, method)
            print(f'# {func.__name__} ({type(func).__name__} of {td.__name__}):  {str(func.__doc__)}')
    else:
        print(f'# {td.__name__} ({type(td).__name__}):  {str(td.__doc__)}')

doc(canisterpy.Canister)
doc(canisterpy.Package)
doc(canisterpy.Repo)