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
    p_rectangle(l, w), p_triangle(a, b, c), a_rectangle(l, w), sa_box(l, w, h), v_box(l, w, h)

Variables
------------------
l: length
w: width
h: height
s: side length
a, c: side length for side 1 and 3 of triangle
b: side length 2 for p_triangle OR the base (b) for a_triangle
r: Radius of circle



Functions
---------
Perimeter:
    p_rectangle(l, w), p_square(s), p_triangle(a, b, c), c_circle(r)

Area:
    a_rectangle(l, w), a_square(s), a_triangle(b, h), a_circle(r)

Surface Area:
    sa_box(l, w, h), sa_sphere(r), sa_cylinder(r, h)

Volume:
    v_box(l, w, h), v_sphere(r), v_cylinder(r, h)

Examples
--------
>>> a_rectangle(5, 3)
15.0
>>> v_sphere(2)
33.510321638291124
"""

from math import pi

__version__ = "0.1.2"
__author__ = "Tyler Nordby"
__license__ = "MIT"
__docformat__ = "numpy"

if __name__ == "__main__":
    print("You have executed the file shapes.py directly instead of using it as a module. Everything works and nothing is wrong.")

# Perimeter/circumference

def p_rectangle(l: int | float, w: int | float) -> float:
    """
    Calculate the perimeter of a rectangle.

    Formula: $$P = 2(l+w)$$

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

    Formula: $$P = 4s$$

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

    Formula: $$P = a + b + c$$

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
    r"""
    Calculate the circumference of a circle.

    Formula: $$C = 2 \pi r$$

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

    Formula: $$A = lw$$

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

    Formula: $$A = s^2$$

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
    r"""
    Calculate the area of a triangle.

    Formula: $$A = \frac{1}{2}bh$$

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
    r"""
    Calculate the area of a circle.

    Formula: $$A = \pi r^2$$

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

    Formula: $$SA = 2lw + 2lh + 2wh$$

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
    r"""
    Calculate the surface area of a sphere.

    Formula: $$SA = 4 \pi r^2$$

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
    r"""
    Calculate the surface area of a cylinder.

    Formula: $$SA = 2 \pi r(r + h)$$

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

    Formula: $$V = lwh$$

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
    r"""
    Calculate the volume of a sphere.

    Formula: $$V = \frac{4}{3} \pi r^3$$

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
    r"""
    Calculate the volume of a cylinder.

    Formula: $$V = \pi r^2 h$$

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





