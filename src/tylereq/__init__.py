""" 
tylereq
=======

A simple equations module made by Tyler.

Currently includes:
-------------------
- `shapes` : geometry-related formulas for perimeters, areas, surface areas, and volumes.

But, I have plans to expand outside of shape related formulas

Examples
--------
>>> import tylereq
>>> tylereq.a_circle(5)
78.53981633974483

>>> from tylereq import p_square
>>> p_square(10)
40
"""

from importlib.metadata import version as _get_version

__version__ = "0.1.0"
__author__ = "Tyler"
__license__ = "MIT"
__docformat__ = "numpy"

try:
    __version__ = _get_version("tylereq")
except Exception:
    __version__ = "0.1.0"

from .shapes import (
    p_rectangle, p_square, p_triangle, c_circle,
    a_rectangle, a_square, a_triangle, a_circle,
    sa_box, sa_sphere, sa_cylinder,
    v_box, v_sphere, v_cylinder,
)

__all__ = [
    # from shapes.py
    "p_rectangle", "p_square", "p_triangle", "c_circle",
    "a_rectangle", "a_square", "a_triangle", "a_circle",
    "sa_box", "sa_sphere", "sa_cylinder",
    "v_box", "v_sphere", "v_cylinder",
]
