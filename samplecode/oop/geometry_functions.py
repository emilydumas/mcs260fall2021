"""
Manipulating geometric objects in the plane using functions
"""
# MCS 260 Fall 2021 Lecture 25

# circle is a list with elements [cx,cy,r]
# rectangle is a list with elements [cx,cy,w,h]

def circle_scale(circle, factor):
    """Modify the circle `circle`, multiplying its radius by 
    the factor `factor`.  (Modify `circle` in place, rather
    than returning the new circle.)"""
    circle[2] *= factor # radius

def rectangle_scale(rectangle, factor):
    """Modify the rectangle `rectangle`, multiplying its width
    and height by factor `factor`.  (Modify `rectangle` in place, rather
    than returning the new rectangle.)"""
    rectangle[2] *= factor # width
    rectangle[3] *= factor # height


