
import enum

from typing import Any, List, Tuple

CH_MetaPath = List[Any]

'''
Transpiler state for component, either stop or continue
'''

class InnerComponentState(enum.Enum):
    ERROR           = -1
    RUNNING         =  0
    STOPPED         =  1
    MIGHT_CONTINUE  =  2

# Transpiler rebuild arguments
CH_ComponentRebuildValue = List[Any]
# Transpiler state to store
CH_ComponentReturnState  = Tuple[InnerComponentState, int, int, CH_ComponentRebuildValue]

from pysm.chronos.component import ChronosComponent

CH_LibC = List[ChronosComponent]
