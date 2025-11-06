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

__author__ = "Tyler"
__license__ = "MIT"
__docformat__ = "numpy"
__version__ = "0.1.1"

__all__ = ["shapes"]

# Quick list of all the functions in shapes
# "p_rectangle", "p_square", "p_triangle", "c_circle", "a_rectangle", "a_square", 
# "a_triangle", "a_circle", "sa_box",  "sa_sphere", "sa_cylinder", "v_box", "v_sphere", "v_cylinder"
