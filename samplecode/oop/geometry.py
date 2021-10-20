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
    def scale(self,factor):
        "Modify the rectangle, multiplying its w and h by `factor`"
        self.w *= factor
        self.h *= factor

class Circle:
    """A circle in the plane represented by its center (cx,cy) and
    radius r."""
    def __init__(self,cx,cy,r):
        "Build a new Circle object from the given center, radius"
        self.cx = cx  # create a new attribute called cx
        self.cy = cy
        self.r = r
    def scale(self,factor):
        "Modify the circle, multiplying its radius by `factor`"
        self.r *= factor

