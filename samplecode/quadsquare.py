# MCS 260 Fall 2021 Lecture 4
# Determine whether a quadratic
# polynomial is a perfect square

# We read a polynomial
#   ax**2 + bx + c
# by asking for a, b, c separately
print("Enter the coefficients a, b, c")
print("of a quadratic polynomial ax**2 + bx + c")
print("one per line.")
a = float(input())
b = float(input())
c = float(input())

# discriminant of ax**2+bx+c is b**2 - 4ac
# discriminant is zero exactly when the poly
# is a perfect square
disc = b*b - 4*a*c

if disc == 0.0:
    print("It's a perfect square!")
