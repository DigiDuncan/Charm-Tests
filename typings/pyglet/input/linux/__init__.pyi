"""
This type stub file was generated by pyright.
"""

from .evdev import EvdevControllerManager as ControllerManager, get_controllers, get_devices as evdev_get_devices, get_joysticks
from .x11_xinput_tablet import get_tablets
from .x11_xinput import get_devices as x11xinput_get_devices

def get_devices(display=...): # -> list[Any]:
    ...

