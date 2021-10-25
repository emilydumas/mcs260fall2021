"""
Manipulating geometric objects in the plane using classes
"""
# MCS 260 Fall 2021 Lecture 25

class Rectangle:
    """A rectangle in the plane represented by its center (cx,cy),
    width w, and height h."""
    def __init__(self,cx,cy,w,h):
        "Build a new Rectangle object from the given center, w, h"
        self.cx = cx  # create a new attribute called cx
        self.cy = cy
        self.w = w
        self.h = h
    def __str__(self):
        "Return a string that represents the object"
        return "Rectangle(cx={},cy={},w={},h={})".format(
            self.cx,
            self.cy,
            self.w,
            self.h,
        )
    def __repr__(self):
        """Return a string that represents the object, when it is
        necessary to display it IN THE PYTHON REPL"""
        # Let's just call the __str__ method we already defined!
        return self.__str__()
    def __eq__(self,other):
        """Return True if Rectangle objects self and other have the
        same center, width, and height"""
        if isinstance(other,Rectangle):
            return self.cx==other.cx and self.cy==other.cy and self.w==other.w and self.h==other.h
        else:
            # The other thing isn't a rectangle
            return False
    def scale(self,factor):
        "Modify the rectangle, multiplying its w and h by `factor`"
        self.w *= factor
        self.h *= factor
    def translate(self,dx,dy):
        "Translate the rectangle by vector (dx,dy)."
        self.cx += dx
        self.cy += dy

class Circle:
    """A circle in the plane represented by its center (cx,cy) and
    radius r."""
    def __init__(self,cx,cy,r):
        "Build a new Circle object from the given center, radius"
        self.cx = cx  # create a new attribute called cx
        self.cy = cy
        self.r = r
    def __str__(self):
        "Return a string that represents the object"
        return "Circle(cx={},cy={},r={})".format(
            self.cx,
            self.cy,
            self.r,
        )
    def __repr__(self):
        """Return a string that represents the object, when it is
        necessary to display it IN THE PYTHON REPL"""
        # Let's just call the __str__ method we already defined!
        return self.__str__()
    def __eq__(self,other):
        """Return True if Circle objects self and other have the
        same center and radius."""
        return self.cx==other.cx and self.cy==other.cy and self.r==other.r
    def scale(self,factor):
        "Modify the circle, multiplying its radius by `factor`"
        self.r *= factor
    def translate(self,dx,dy):
        "Translate the circle by vector (dx,dy)."
        self.cx += dx
        self.cy += dy
