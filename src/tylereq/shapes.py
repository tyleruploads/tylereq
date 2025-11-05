# shapes.py - Helper module for tylereq - Hosts functions for 2D and 3D shapes

"""
shapes.py
=================

Helper module for tylereq. Hosts functions for 2D and 3D shapes

A lightweight geometry helper module for calculating perimeters, areas,
surface areas, and volumes of common 2D and 3D shapes.

Function Naming Conventions
------------------
All functions include a prefix (what you are calculating with an _ after) and a suffix (the shape).

Prefixes:
- p_ : perimeter
- c_ : circumference
- a_ : area
- sa_ : surface area
- v_ : volume

Examples:
    p_rectangle, p_triangle, a_rectangle, sa_box, v_box

Variables
------------------
l: length
w: width
h: height
s: side length
a, b, c: side length for side 1, 2, and 3 or triangle
b: When used in a function with the suffix _triangle, represents the base of the triangle
r: Radius of circle



Functions
---------
Perimeter:
    p_rectangle, p_square, p_triangle, c_circle

Area:
    a_rectangle, a_square, a_triangle, a_circle

Surface Area:
    sa_box, sa_sphere, sa_cylinder

Volume:
    v_box, v_sphere, v_cylinder

Examples
--------
>>> a_rectangle(5, 3)
15.0
>>> v_sphere(2)
33.510321638291124
"""

from math import pi

__version__ = "1.0.0"
__author__ = "Tyler Nordby"
__license__ = "MIT"
__docformat__ = "numpy"

if __name__ == "__main__":
    print("You have executed the file shapes.py directly instead of using it as a module. Everything works and nothing is wrong.")

# Perimeter/circumference

def p_rectangle(l: int | float, w: int | float) -> float:
    """
    Calculate the perimeter of a rectangle.

    Parameters
    ----------
    l : int | float
        The length of the rectangle.
    w : int | float
        The width of the rectangle.

    Returns
    -------
    float
        The perimeter of the rectangle.
    """
    p = 2 * (l + w)
    return p

def p_square(s: int | float) -> float:
    """
    Calculate the perimeter of a square.

    Parameters
    ----------
    s : int | float
        The side length of the square.

    Returns
    -------
    float
        The perimeter of the square.
    """
    p = 4 * s
    return p

def p_triangle(a: int | float, b: int | float, c: int | float) -> float:
    """
    Calculate the perimeter of a triangle.

    Parameters
    ----------
    a : int | float
        The side length of side A of the triangle.
    b : int | float
        The side length of side B of the triangle.
    c : int | float
        The side length of side C of the triangle.

    Returns
    -------
    float
        The perimeter of the triangle.
    """
    p = a + b + c
    return p

#def p_trapezoid(): 
# DO LATER I HAVE NO CLUE ABOUT THIS

# Same with isoceles trapezoid

def c_circle(r: int | float) -> float:
    """
    Calculate the circumference of a circle.

    Parameters
    ----------
    r : int | float
        The radius of the circle.

    Returns
    -------
    float
        The circumference of the circle.
    """
    c = 2 * pi * r
    return c

# --- AREA! ---

def a_rectangle(l: int | float, w: int | float) -> float:
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    l : int | float
        The length of the rectangle.
    w : int | float
        The width of the rectangle.

    Returns
    -------
    float
        The area of the rectangle.
    """
    a = l * w
    return a

def a_square(s: int | float) -> float:
    """
    Calculate the area of a square.

    Parameters
    ----------
    s : int | float
        A singular side length of the square.

    Returns
    -------
    float
        The area of the square.
    """
    a = s**2
    return a
    
def a_triangle(b: int | float, h: int | float) -> float:
    """
    Calculate the area of a triangle.

    Parameters
    ----------
    b : int | float
        The base of the triangle.
    h : int | float
        The height of the triangle.

    Returns
    -------
    float
        The area of the triangle.
    """
    a = (1/2) * (b * h)
    return a

# Do trapezoid and isoceles trapezoid later

def a_circle(r: int | float) -> float:
    """
    Calculate the area of a circle.

    Parameters
    ----------
    r : int | float
        The radius of the circle.

    Returns
    -------
    float
        The area of the circle.
    """
    a = pi * (r**2)
    return a

# --- SURFACE AREA ---

def sa_box(l: int | float, w: int | float, h: int | float) -> float:
    """
    Calculate the surface area of a box (rectangular prism).

    Parameters
    ----------
    l : int | float
        The length of the box.
    w : int | float
        The width of the box.
    h : int | float
        The height of the box.

    Returns
    -------
    float
        The surface area of the box.
    """
    sa = 2*l*w + 2*l*h + 2*w*h
    return sa

def sa_sphere(r: int | float) -> float:
    """
    Calculate the surface area of a sphere.

    Parameters
    ----------
    r : int | float
        The radius of the sphere.

    Returns
    -------
    float
        The surface area of the sphere.
    """
    sa = 4 * pi * (r**2)
    return sa

def sa_cylinder(r: int | float, h: int | float) -> float:
    """
    Calculate the surface area of a cylinder.

    Parameters
    ----------
    r : int | float
        The radius of the cylinder.
    h : int | float
        The height of the cylinder.

    Returns
    -------
    float
        The surface area of the cylinder.
    """
    sa = 2 * pi * r * (r + h)
    return sa

# --- VOLUME ---

def v_box(l: int | float, w: int | float, h: int | float) -> float:
    """
    Calculate the volume of a box (rectangular prism).

    Parameters
    ----------
    l : int | float
        The length of the box.
    w : int | float
        The width of the box.
    h : int | float
        The height of the box.

    Returns
    -------
    float
        The volume of the box.
    """
    v = l * w * h
    return v

def v_sphere(r: int | float) -> float:
    """
    Calculate the volume of a sphere.

    Parameters
    ----------
    r : int | float
        The radius of the sphere.

    Returns
    -------
    float
        The volume of the sphere.
    """
    v = (4/3) * pi * (r**3)
    return v

def v_cylinder(r: int | float, h: int | float) -> float:
    """
    Calculate the volume of a cylinder.

    Parameters
    ----------
    r : int | float
        The radius of the cylinder.
    h : int | float
        The height of the cylinder.

    Returns
    -------
    float
        The volume of the cylinder.
    """
    v = pi * (r**2) * h
    return v

__all__ = [
    "p_rectangle", "p_square", "p_triangle", "c_circle",
    "a_rectangle", "a_square", "a_triangle", "a_circle",
    "sa_box", "sa_sphere", "sa_cylinder",
    "v_box", "v_sphere", "v_cylinder",
]





