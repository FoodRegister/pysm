
from importlib.machinery        import ModuleSpec
from pysm.chronos.router.loader import MetaPathLoader
from pysm.chronos.router.types  import CH_MetaPath

import os

class MetaPathImporter(object):
    def __init__(self, meta_path : CH_MetaPath):
        self.meta_path = meta_path
    
    def find_module(self, module_name, package_path):
        package_data = module_name.split(".")[:-1]
        if  len(package_data) > 0    \
        and package_path is not None \
        and len(package_path) == 0:
            package_path = self.find_parent_path(module_name)
        print(module_name, package_path)
        
        for path_finder in self.meta_path:
            loader = path_finder.find_module(module_name, package_path)

            if loader is not None:
                return MetaPathLoader(module_name, package_path, loader.path)
        raise ValueError("Could not find ", package_path, module_name)
    def find_spec(self, module_name, package_path, uk):
        loader = self.find_module(module_name, package_path)

        specs = ModuleSpec(
            loader.get_name(), 
            loader, 
            origin=loader.get_path(), 
            is_package=loader.is_package(),
        )

        if loader.is_package(): specs.submodule_search_locations = [ 
            loader.get_path()[:-11] if loader.get_path().endswith("__init__.py") else loader.get_path()
        ]

        return specs
    def find_parent_path(self, module_name):
        first_module = module_name.split(".")[0]
        next_modules = module_name.split(".")[1:-1]
        print(first_module, next_modules)
        next_modpath = "" if len(next_modules) == 0 else os.path.join(*next_modules)

        pathes = self.find_spec(first_module, None, "").submodule_search_locations

        return list(map(lambda x: os.path.join(x, next_modpath), pathes))

class MetaPathContainer:
    def __init__(self, meta_path_importer : MetaPathImporter):
        self.meta_path_importer = meta_path_importer
        self.forward_functions  = [ 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort' ]
    def __len__(self):
        return 1
    def __getitem__(self, index):
        return self.meta_path_importer
    def __iter__(self):
        yield self.meta_path_importer
    def __getattribute__(self, __name: str):
        if __name == "forward_functions": return super().__getattribute__(__name)
        if __name in self.forward_functions: return getattr(self.meta_path_importer.meta_path, __name)
        return super().__getattribute__(__name)
