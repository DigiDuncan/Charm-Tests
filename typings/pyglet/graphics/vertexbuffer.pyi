"""
This type stub file was generated by pyright.
"""

from functools import lru_cache
from pyglet.gl import *

"""Byte abstractions of OpenGL Buffer Objects.

Use `create_buffer` to create a Buffer Object.

Buffers can optionally be created "mappable" (incorporating the
`AbstractMappable` mix-in).  In this case the buffer provides a ``get_region``
method which provides the most efficient path for updating partial data within
the buffer.
"""
class AbstractBuffer:
    """Abstract buffer of byte data.

    :Ivariables:
        `size` : int
            Size of buffer, in bytes
        `ptr` : int
            Memory offset of the buffer, as used by the ``glVertexPointer``
            family of functions
        `usage` : int
            OpenGL buffer usage, for example ``GL_DYNAMIC_DRAW``

    """
    ptr = ...
    size = ...
    def bind(self, target=...):
        """Bind this buffer to an OpenGL target."""
        ...
    
    def unbind(self):
        """Reset the buffer's OpenGL target."""
        ...
    
    def set_data(self, data):
        """Set the entire contents of the buffer.

        :Parameters:
            `data` : sequence of int or ctypes pointer
                The byte array to set.

        """
        ...
    
    def set_data_region(self, data, start, length):
        """Set part of the buffer contents.

        :Parameters:
            `data` : sequence of int or ctypes pointer
                The byte array of data to set
            `start` : int
                Offset to start replacing data
            `length` : int
                Length of region to replace

        """
        ...
    
    def map(self):
        """Map the entire buffer into system memory.

        The mapped region must be subsequently unmapped with `unmap` before
        performing any other operations on the buffer.

        :Parameters:
            `invalidate` : bool
                If True, the initial contents of the mapped block need not
                reflect the actual contents of the buffer.

        :rtype: ``POINTER(ctypes.c_ubyte)``
        :return: Pointer to the mapped block in memory
        """
        ...
    
    def unmap(self):
        """Unmap a previously mapped memory block."""
        ...
    
    def resize(self, size): # -> None:
        """Resize the buffer to a new size.

        :Parameters:
            `size` : int
                New size of the buffer, in bytes

        """
        ...
    
    def delete(self):
        """Delete this buffer, reducing system resource usage."""
        ...
    


class BufferObject(AbstractBuffer):
    """Lightweight representation of an OpenGL Buffer Object.

    The data in the buffer is not replicated in any system memory (unless it
    is done so by the video driver).  While this can improve memory usage and
    possibly performance, updates to the buffer are relatively slow.
    The target of the buffer is ``GL_ARRAY_BUFFER`` internally to avoid
    accidentally overriding other states when altering the buffer contents.
    The intended target can be set when binding the buffer.

    This class does not implement :py:class:`AbstractMappable`, and so has no
    :py:meth:`~AbstractMappable.get_region` method.  See 
    :py:class:`MappableVertexBufferObject` for a Buffer class
    that does implement :py:meth:`~AbstractMappable.get_region`.
    """
    def __init__(self, size, usage=...) -> None:
        ...
    
    def invalidate(self): # -> None:
        ...
    
    def bind(self, target=...): # -> None:
        ...
    
    def unbind(self): # -> None:
        ...
    
    def bind_to_index_buffer(self): # -> None:
        """Binds this buffer as an index buffer on the active vertex array."""
        ...
    
    def set_data(self, data): # -> None:
        ...
    
    def set_data_region(self, data, start, length): # -> None:
        ...
    
    def map(self): # -> Array[c_byte]:
        ...
    
    def map_range(self, start, size, ptr_type):
        ...
    
    def unmap(self): # -> None:
        ...
    
    def delete(self): # -> None:
        ...
    
    def __del__(self): # -> None:
        ...
    
    def resize(self, size): # -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    


class AttributeBufferObject(BufferObject):
    """A buffer with system-memory backed store.

    Updates to the data via `set_data` and `set_data_region` will be held
    in local memory until `buffer_data` is called.  The advantage is that
    fewer OpenGL calls are needed, which can increasing performance at the
    expense of system memory.
    """
    def __init__(self, size, attribute, usage=...) -> None:
        ...
    
    def sub_data(self): # -> None:
        """Updates the buffer if any data has been changed or invalidated. Allows submitting multiple changes at once,
        rather than having to call glBufferSubData for every change."""
        ...
    
    @lru_cache(maxsize=None)
    def get_region(self, start, count):
        ...
    
    def set_region(self, start, count, data): # -> None:
        ...
    
    def resize(self, size): # -> None:
        ...
    
    def invalidate(self): # -> None:
        ...
    
    def invalidate_region(self, start, count): # -> None:
        ...
    


class PersistentBufferObject(AbstractBuffer):
    def __init__(self, size, attribute, vao) -> None:
        ...
    
    def bind(self, target=...): # -> None:
        ...
    
    def unbind(self): # -> None:
        ...
    
    def map_range(self, start, size, ptr_type, flags=...):
        ...
    
    @lru_cache(maxsize=None)
    def get_region(self, start, count):
        ...
    
    def set_region(self, start, count, data): # -> None:
        ...
    
    def resize(self, size): # -> None:
        ...
    
    def sub_data(self): # -> None:
        ...
    
    def invalidate(self): # -> None:
        ...
    
    def invalidate_region(self, start, count): # -> None:
        ...
    


