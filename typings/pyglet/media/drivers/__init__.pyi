"""
This type stub file was generated by pyright.
"""

import sys
import atexit
import pyglet
from . import silent

"""Drivers for playing back media."""
_debug = pyglet.options['debug_media']
_is_pyglet_doc_run = ...
if _is_pyglet_doc_run:
    _audio_driver = ...
else:
    ...
def get_audio_driver(): # -> SilentDriver | PulseAudioDriver | XAudio2Driver | DirectSoundDriver | OpenALDriver | None:
    """Get the preferred audio driver for the current platform.

    See :data:`pyglet.options` ``audio``, and the Programming guide,
    section :doc:`/programming_guide/media` for more information on
    setting the preferred driver.

    Returns:
        AbstractAudioDriver : The concrete implementation of the preferred
                              audio driver for this platform.
    """
    ...
