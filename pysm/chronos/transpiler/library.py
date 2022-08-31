
from typing             import List, Tuple
from tokenize           import TokenInfo, tokenize, untokenize
from pysm.chronos.transpiler.scheme import Scheme
from pysm.chronos.types import CH_ComponentReturnState, CH_LibC, InnerComponentState
from pysm.chronos.component import ChronosComponent

class Library:
    def __init__(self, components: CH_LibC):
        self.components = components
    def to_tokens  (self, code: str): return list(tokenize(bytes(code, encoding="utf-8")))
    def from_tokens(self, tokens: List[TokenInfo]) -> str:
        # TODO rebuild tokens for syntax

        # SUB-TODO rebuild everything whitout line gap
        # SUB-TODO remove air gaps

        return untokenize(tokens).decode(encoding="utf-8")

    def make_scheme(self, tokens: List[TokenInfo]) -> List[Scheme]:
        component_stack : List[Scheme] = []
        schemes : List[Scheme] = []
        tok_idx = 0
        
        def can_close() -> CH_ComponentReturnState:
            if len(component_stack) == 0: return None
            return component_stack[-1].component.is_viable(tokens, tok_idx, component_stack[-1].component_state)
        def get_scheme() -> Tuple[CH_ComponentReturnState, ChronosComponent, bool]:
            close_scheme = can_close()
            if close_scheme is not None: return close_scheme, component_stack[-1].component, True

            for component in self.components:
                try: 
                    inner_state, component_state, token_count, args = component.is_viable(tokens, tok_idx, component.get_first_component_state())
                except Exception: continue

                if inner_state == InnerComponentState.ERROR: continue
                
                return (inner_state, component_state, token_count, args), component, False
            
            return None

        while tok_idx < len(tokens):
            partial_scheme = get_scheme()

            if partial_scheme is None:
                tok_idx += 1
                continue
            
            data_scheme, component, close = partial_scheme
            inner_state, component_state, token_count, args = data_scheme

            if close: component_stack.pop()

            scheme = Scheme(component, args, tok_idx, component_state)
            if inner_state != InnerComponentState.STOPPED:
                component_stack.append(scheme)
            schemes.append(scheme)

        return schemes # TODO from components to scheme
    def restore_scheme(self, tokens: List[TokenInfo], scheme: List[Scheme]):
        pass # TODO update tokens with scheme in reverse order

    def transpile (self, code: str) -> str:
        tokens = self.to_tokens(code)

        scheme = self.make_scheme(tokens)
        self.restore_scheme(tokens, scheme)

        return self.from_tokens(tokens)
