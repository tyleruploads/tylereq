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
area = shapes.a_rectangle(5, 3)  # Returns 15.0

# Calculate volume of a sphere
volume = shapes.v_sphere(2)  # Returns 33.510321638291124

# Calculate perimeter of a square
perimeter = shapes.p_square(10)  # Returns 40
```

## Available Functions

### Perimeter/Circumference
- `p_rectangle(l, w)`: Rectangle perimeter
- `p_square(s)`: Square perimeter
- `p_triangle(a, b, c)`: Triangle perimeter
- `c_circle(r)`: Circle circumference

### Area
- `a_rectangle(l, w)`: Rectangle area
- `a_square(s)`: Square area
- `a_triangle(b, h)`: Triangle area
- `a_circle(r)`: Circle area

### Surface Area
- `sa_box(l, w, h)`: Box surface area
- `sa_sphere(r)`: Sphere surface area
- `sa_cylinder(r, h)`: Cylinder surface area

### Volume
- `v_box(l, w, h)`: Box volume
- `v_sphere(r)`: Sphere volume
- `v_cylinder(r, h)`: Cylinder volume

## Documentation

Full documentation is available at the project's GitHub Pages site.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
