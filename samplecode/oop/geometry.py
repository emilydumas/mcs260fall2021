"""
Geometric objects in the plane
"""
# MCS 260 Fall 2021 Lecture 25, 26, 27

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
    # Suppose R and S are rectangles
    # Then R == S ultimately calls
    # R.__eq__(S)
    # so the method below is called with
    #          R-\/ S-\/
    def __eq__(self,other):
        """Return True if Rectangle objects self and other have the
        same center, width, and height"""
        if isinstance(other,Rectangle):
            return self.cx==other.cx and self.cy==other.cy and self.w==other.w and self.h==other.h
        else:
            # The other thing isn't a rectangle
            return False
    # R + S
    # becomes
    # R.__add__(S)
    # which calls the method defined below with
    #           R    S
    def __add__(self,other):
        """Compute the bounding box of Rectangles self and other"""
        # largest x coordinate of either rectangle
        xmax = max(self.cx + 0.5*self.w,other.cx + 0.5*other.w)
        # smallest x coordinate of either rectangle
        xmin = min(self.cx - 0.5*self.w,other.cx - 0.5*other.w)
        # largest y coordinate of either rectangle
        ymax = max(self.cy + 0.5*self.h,other.cy + 0.5*other.h)
        # smallest y coordinate of either rectangle
        ymin = min(self.cy - 0.5*self.h,other.cy - 0.5*other.h)
    
        # Convert min/max x and y values for the bounding box
        # into its center, width, and height
        bb_cx = 0.5*(xmax+xmin)
        bb_cy = 0.5*(ymax+ymin)
        bb_w = xmax - xmin
        bb_h = ymax - ymin

        return Rectangle(bb_cx,bb_cy,bb_w,bb_h)

    def scale(self,factor):
        "Modify the rectangle, multiplying its w and h by `factor`"
        self.w *= factor
        self.h *= factor
    def translate(self,dx,dy):
        "Translate the rectangle by vector (dx,dy)."
        self.cx += dx
        self.cy += dy

#     Square extends Rectangle 
class Square(Rectangle):
    """A square in the plane represented by its center (cx,cy)
    and its side length `side`."""
    def __init__(self,cx,cy,side):
        """Build a new Square instance with the given center and
        side length"""
        # Call the constructor of Rectangle with (cx,cy,side,side)
        super().__init__(cx,cy,side,side)
        # The line above is equivalent to:
        # self.cx = cx
        # self.cy = cy
        # self.w = side
        # self.h = side
    def __str__(self):
        """Human-readable string representation"""
        return "Square(cx={},cy={},side={})".format(
            self.cx,
            self.cy,
            self.w,
        )

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
