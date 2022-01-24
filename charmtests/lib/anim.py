import math

from .utils import clamp

def time_to_zero_one_ramp(start: float, end: float, time: float) -> float:
    """Convert a time to its progress through the range start -> end, from 0 to 1.
    
    https://www.desmos.com/calculator/d2qdk3lceh"""
    y = ((1 / (end - start)) * time) - (start / (end - start))
    return clamp(0, y, 1)


def zero_one_to_range(start: float, end: float, i: float) -> float:
    """Convert a number between 0 and 1 to be the progress within a range start -> end."""
    return start + (i * (end - start))
    

def bounce(n: float, m: float, s: float, x: float) -> float:
    """Create a bouncing motion between max(0, n) and m with period 1/s at time x."""
    return max(abs(math.sin(x * math.pi * s)) * m, n)

def ease_linear(minimum: float, maximum: float, start: float, end: float, x: float) -> float:
    """* `minimum: float`: the value returned by f(`x`) = `start`, often a position
       * `maximum: float`: the value returned by f(`x`) = `end`, often a position
       * `start: float`: the beginning of the transition, often a time
       * `end: float`: the end of the transition, often a time
       * `x: float`: the current x, often a time"""
    x = time_to_zero_one_ramp(start, end, x)
    return zero_one_to_range(minimum, maximum, x)

def ease_quadinout(minimum: float, maximum: float, start: float, end: float, x: float) -> float:
    """https://easings.net/#easeInOutQuad"""
    x = time_to_zero_one_ramp(start, end, x)
    if x < 0.5:
        zo = 2 * x * x
    else:
        zo = 1 - math.pow(-2 * x + 2, 2) / 2
    return zero_one_to_range(minimum, maximum, zo)
