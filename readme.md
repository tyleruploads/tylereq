# tylereq

A simple equations module made by Tyler, providing geometry-related formulas for perimeters, areas, surface areas, and volumes.

## Installation

```bash
pip install tylereq
```

## Usage

```python
from tylereq import shapes

# Calculate area of a rectangle
area = tylereq.shapes.a_rectangle(5, 3)  # Returns 15.0

# Calculate volume of a sphere
volume = tylereq.shapes.v_sphere(2)  # Returns 33.510321638291124

# Calculate perimeter of a square
perimeter = tylereq.shapes.p_square(10)  # Returns 40
```

## Available Functions

### Perimeter/Circumference
- `tylereq.shapes.p_rectangle(l, w)`: Rectangle perimeter
- `tylereq.shapes.p_square(s)`: Square perimeter
- `tylereq.shapes.p_triangle(a, b, c)`: Triangle perimeter
- `tylereq.shapes.c_circle(r)`: Circle circumference

### Area
- `tylereq.shapes.a_rectangle(l, w)`: Rectangle area
- `tylereq.shapes.a_square(s)`: Square area
- `tylereq.shapes.a_triangle(b, h)`: Triangle area
- `tylereq.shapes.a_circle(r)`: Circle area

### Surface Area
- `tylereq.shapes.sa_box(l, w, h)`: Box surface area
- `tylereq.shapes.sa_sphere(r)`: Sphere surface area
- `tylereq.shapes.sa_cylinder(r, h)`: Cylinder surface area

### Volume
- `tylereq.shapes.v_box(l, w, h)`: Box volume
- `tylereq.shapes.v_sphere(r)`: Sphere volume
- `tylereq.shapes.v_cylinder(r, h)`: Cylinder volume

## Documentation

Full documentation is available at the project's GitHub Pages site.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
