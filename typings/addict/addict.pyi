"""
This type stub file was generated by pyright.
"""

class Dict(dict):
    def __init__(__self, *args, **kwargs) -> None:
        ...
    
    def __setattr__(self, name, value): # -> None:
        ...
    
    def __setitem__(self, name, value): # -> None:
        ...
    
    def __add__(self, other):
        ...
    
    def __getattr__(self, item):
        ...
    
    def __missing__(self, name): # -> Self:
        ...
    
    def __delattr__(self, name): # -> None:
        ...
    
    def to_dict(self): # -> dict[Any, Any]:
        ...
    
    def copy(self): # -> Self:
        ...
    
    def deepcopy(self): # -> Self:
        ...
    
    def __deepcopy__(self, memo): # -> Self:
        ...
    
    def update(self, *args, **kwargs): # -> None:
        ...
    
    def __getnewargs__(self): # -> tuple[tuple[Any, Any], ...]:
        ...
    
    def __getstate__(self): # -> Self:
        ...
    
    def __setstate__(self, state): # -> None:
        ...
    
    def __or__(self, other): # -> _NotImplementedType | Dict:
        ...
    
    def __ror__(self, other): # -> _NotImplementedType | Dict:
        ...
    
    def __ior__(self, other): # -> Self:
        ...
    
    def setdefault(self, key, default=...): # -> None:
        ...
    
    def freeze(self, shouldFreeze=...): # -> None:
        ...
    
    def unfreeze(self): # -> None:
        ...
    


