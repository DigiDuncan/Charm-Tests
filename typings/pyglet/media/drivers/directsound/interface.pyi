"""
This type stub file was generated by pyright.
"""

"""
Pythonic interface to DirectSound.
"""
_debug = ...
class DirectSoundDriver:
    def __init__(self) -> None:
        ...
    
    def delete(self): # -> None:
        ...
    
    def create_buffer(self, audio_format, buffer_size): # -> DirectSoundBuffer:
        ...
    
    def create_listener(self): # -> DirectSoundListener:
        ...
    


_CurrentPosition = ...
class DirectSoundBuffer:
    def __init__(self, native_buffer, audio_format, buffer_size) -> None:
        ...
    
    def delete(self): # -> None:
        ...
    
    @property
    def volume(self): # -> int:
        ...
    
    @volume.setter
    def volume(self, value): # -> None:
        ...
    
    @property
    def current_position(self): # -> _CurrentPosition:
        """Tuple of current play position and current write position.
        Only play position can be modified, so setter only accepts a single value."""
        ...
    
    @current_position.setter
    def current_position(self, value): # -> None:
        ...
    
    @property
    def is3d(self): # -> bool:
        ...
    
    @property
    def is_playing(self): # -> bool:
        ...
    
    @property
    def is_buffer_lost(self): # -> bool:
        ...
    
    @property
    def position(self): # -> tuple[Any, Any, Any] | tuple[Literal[0], Literal[0], Literal[0]]:
        ...
    
    @position.setter
    def position(self, position): # -> None:
        ...
    
    @property
    def min_distance(self): # -> float | Literal[0]:
        """The minimum distance, which is the distance from the
        listener at which sounds in this buffer begin to be attenuated."""
        ...
    
    @min_distance.setter
    def min_distance(self, value): # -> None:
        ...
    
    @property
    def max_distance(self): # -> float | Literal[0]:
        """The maximum distance, which is the distance from the listener beyond which
        sounds in this buffer are no longer attenuated."""
        ...
    
    @max_distance.setter
    def max_distance(self, value): # -> None:
        ...
    
    @property
    def frequency(self): # -> int:
        ...
    
    @frequency.setter
    def frequency(self, value): # -> None:
        """The frequency, in samples per second, at which the buffer is playing."""
        ...
    
    @property
    def cone_orientation(self): # -> tuple[Any, Any, Any] | tuple[Literal[0], Literal[0], Literal[0]]:
        """The orientation of the sound projection cone."""
        ...
    
    @cone_orientation.setter
    def cone_orientation(self, value): # -> None:
        ...
    
    _ConeAngles = ...
    @property
    def cone_angles(self): # -> _ConeAngles:
        """The inside and outside angles of the sound projection cone."""
        ...
    
    def set_cone_angles(self, inside, outside): # -> None:
        """The inside and outside angles of the sound projection cone."""
        ...
    
    @property
    def cone_outside_volume(self): # -> int:
        """The volume of the sound outside the outside angle of the sound projection cone."""
        ...
    
    @cone_outside_volume.setter
    def cone_outside_volume(self, value): # -> None:
        ...
    
    def create_listener(self): # -> DirectSoundListener:
        ...
    
    def play(self): # -> None:
        ...
    
    def stop(self): # -> None:
        ...
    
    class _WritePointer:
        def __init__(self) -> None:
            ...
        
    
    
    def lock(self, write_cursor, write_size): # -> _WritePointer:
        ...
    
    def unlock(self, pointer): # -> None:
        ...
    


class DirectSoundListener:
    def __init__(self, native_listener) -> None:
        ...
    
    def delete(self): # -> None:
        ...
    
    @property
    def position(self): # -> tuple[Any, Any, Any]:
        ...
    
    @position.setter
    def position(self, value): # -> None:
        ...
    
    @property
    def orientation(self): # -> tuple[Any, Any, Any, Any, Any, Any]:
        ...
    
    @orientation.setter
    def orientation(self, orientation): # -> None:
        ...
    


