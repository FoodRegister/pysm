
import sys

from pysm.chronos.router.metapath import MetaPathContainer, MetaPathImporter

def init_router():
    sys.meta_path = MetaPathContainer(MetaPathImporter(sys.meta_path))

