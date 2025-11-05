from tylereq import shapes
import math

def test_p_rectangle():
    assert shapes.p_rectangle(4, 2) == 12

def test_p_square():
    assert shapes.p_square(5) == 20

def test_p_triangle():
    assert shapes.p_triangle(3, 4, 5) == 12

def test_c_circle():
    assert math.isclose(shapes.c_circle(2), 12.5663706144, rel_tol=1e-5)

def test_a_rectangle():
    assert shapes.a_rectangle(4, 2) == 8

def test_a_square():
    assert shapes.a_square(3) == 9

def test_a_triangle():
    assert shapes.a_triangle(4, 3) == 6

def test_a_circle():
    assert math.isclose(shapes.a_circle(2), 12.5663706144, rel_tol=1e-5)

def test_v_box():
    assert shapes.v_box(2, 3, 4) == 24

def test_v_sphere():
    assert math.isclose(shapes.v_sphere(2), 33.5103216383, rel_tol=1e-5)

def test_v_cylinder():
    assert math.isclose(shapes.v_cylinder(2, 4), 50.2654824574, rel_tol=1e-5)
