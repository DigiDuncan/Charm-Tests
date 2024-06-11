"""
This type stub file was generated by pyright.
"""

def load(*args, **kwargs): # -> Any:
    ...

def loads(*args, **kwargs): # -> Any:
    ...

def dump(obj, fp, cls=..., **kwargs): # -> None:
    ...

def dumps(*args, **kwargs): # -> str:
    ...

class writer:
    def __init__(self, f, **kwargs) -> None:
        ...
    
    def writerow(self, row): # -> None:
        ...
    


class reader:
    def __init__(self, f, **kwargs) -> None:
        ...
    
    def __iter__(self): # -> Self:
        ...
    
    def __next__(self): # -> Any:
        ...
    
    def next(self): # -> Any:
        ...
    


