
'''
Chronos import router. Reroutes an import to allow jit transpilation from extended syntax to standard syntax
'''

import builtins
import importlib

__old_import__ = __import__

def import_router(name, local_var, globals, fromlist, level):
    path = importlib.util.find_spec(name).origin
    
    with open(path, 'r') as file:
        code = file.read()
    code = compile(code, path, "exec")

    globals['__file__'] = path
    globals['__name__'] = name.split(".")[-1]
    globals['__package__'] = ".".join(name.split(".")[:-1])
    if globals['__package__'] == "":
        globals['__package__'] = None
    globals['__cached__']  = None

    exec(code, globals, local_var)

    return locals()

def init_router():
    builtins.__import__ = import_router

