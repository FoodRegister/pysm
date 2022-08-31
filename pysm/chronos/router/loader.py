
import imp
import sys
import os

class MetaPathLoader:
    def __init__(self, name: str, package: str, path: str):
        self.__name = name
        self.__pckg = package
        self.__path = path
    def get_name(self) -> str: return self.__name
    def get_pckg(self) -> str: return self.__pckg
    def get_path(self) -> str: return self.__path
    
    def get_code(self, fullname: str) -> str:
        text = ""
        with open(self.__path, 'r') as file:
            text = file.read()

        return text
    def is_package(self, fullname: str = None) -> bool:
        return self.__path.endswith("__init__.py") or os.path.isdir(self.__path)
    
    def load_module(self, fullname: str):
        code  = self.get_code(fullname)
        ispkg = self.is_package(fullname)

        mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        mod.__file__ = "<%s>" % self.__class__.__name__
        mod.__loader__ = self
        if ispkg:
            mod.__path__ = []
            mod.__package__ = fullname
        else:
            mod.__package__ = fullname.rpartition('.')[0]
        
        exec(code, mod.__dict__)
        
        return mod

