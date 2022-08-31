
from pysm.chronos.component import ChronosComponent
from pysm.chronos.types import CH_ComponentRebuildValue

class Scheme:
    def __init__(self, component: ChronosComponent, args: CH_ComponentRebuildValue, token_idx: int, component_state: int):
        self.args            = args
        self.component       = component
        self.token_idx       = token_idx
        self.component_state = component_state
