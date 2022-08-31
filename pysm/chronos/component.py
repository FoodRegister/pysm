
from pysm.chronos.types import *

class ChronosComponent:
    def __init__(self): raise ValueError("pysm.chronos.ChronosComponent cannot be instantiated")
    def is_viable(
            self, 
            tokens, 
            index  : int, 
            component_state : int
        ) -> CH_ComponentReturnState:
        
        return InnerComponentState.STOPPED, component_state, 1, []
    def get_first_component_state() -> int: return 0

