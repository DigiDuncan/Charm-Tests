"""
This type stub file was generated by pyright.
"""

from typing import Any, TypeVar, overload
from numpy import complexfloating, floating, generic, integer
from numpy._typing import ArrayLike, NDArray, _ArrayLike, _ArrayLikeComplex_co, _ArrayLikeFloat_co, _ShapeLike

_SCT = TypeVar("_SCT", bound=generic)
__all__: list[str]
@overload
def fftshift(x: _ArrayLike[_SCT], axes: None | _ShapeLike = ...) -> NDArray[_SCT]:
    ...

@overload
def fftshift(x: ArrayLike, axes: None | _ShapeLike = ...) -> NDArray[Any]:
    ...

@overload
def ifftshift(x: _ArrayLike[_SCT], axes: None | _ShapeLike = ...) -> NDArray[_SCT]:
    ...

@overload
def ifftshift(x: ArrayLike, axes: None | _ShapeLike = ...) -> NDArray[Any]:
    ...

@overload
def fftfreq(n: int | integer[Any], d: _ArrayLikeFloat_co = ...) -> NDArray[floating[Any]]:
    ...

@overload
def fftfreq(n: int | integer[Any], d: _ArrayLikeComplex_co = ...) -> NDArray[complexfloating[Any, Any]]:
    ...

@overload
def rfftfreq(n: int | integer[Any], d: _ArrayLikeFloat_co = ...) -> NDArray[floating[Any]]:
    ...

@overload
def rfftfreq(n: int | integer[Any], d: _ArrayLikeComplex_co = ...) -> NDArray[complexfloating[Any, Any]]:
    ...

