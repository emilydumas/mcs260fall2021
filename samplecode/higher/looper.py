"Example of higher-order function"
# MCS 260 Fall 2021 Lecture 24
# https://www.dumas.io/teaching/2021/fall/mcs260/slides/lecture24.html#/5


# This is the higher-order function
def loop100(incr):
    """Set a variable to 1, then repeatedly print the value
    and apply `incr` until the value is greater than or equal
    to 100"""
    x = 1
    while x < 100:
        print(x)
        x = incr(x)


# Auxillary functions below


def plus3(x):
    "add 3 to x and return"
    # I include docstrings even when code is obvious
    # because including them is a good habit to build
    return x + 3


def times4(x):
    "multiply x by 4 and return"
    return x * 4


# Main program
print("Using plus3:")
loop100(plus3)
print("Using times4:")
loop100(times4)
