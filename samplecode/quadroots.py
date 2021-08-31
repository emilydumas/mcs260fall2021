# MCS 260 Fall 2021 Lecture 4
# Determine the number of real roots of
# a quadratic polynomial

# We read a polynomial
#   ax**2 + bx + c
# by asking for a, b, c separately
print("Enter the coefficients a, b, c")
print("of a quadratic polynomial ax**2 + bx + c")
print("one per line.")
a = float(input())
b = float(input())
c = float(input())

print("Concerning the quadratic polynomial")
print(a,"x**2 +",b,"x +",c)

# discriminant of ax**2+bx+c is b**2 - 4ac
# discriminant is zero exactly when the poly
# is a perfect square
disc = b*b - 4*a*c

# disc < 0   means no real roots
# disc == 0  means one real root
# disc > 0   means two real roots

# TODO: Handle the case where a is zero
# reporting that it isn't actually a quadratic!
if disc < 0.0:
    print("This polynomial has no real roots.")
elif disc == 0.0:
    print("This polynomial has exactly one real root.")
    print("(It's a perfect square.)")
else:
    print("This polynomial has two real roots.")
