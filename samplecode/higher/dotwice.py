"Example of higher-order functions"
# MCS 260 Fall 2021 Lecture 24


# This is the higher-order function
def dotwice(f):
    """Call the function f twice (with no arguments)"""
    f()
    f()


# Auxillary functions below


def greeting():
    "Print a greeting"
    print("Hello!")


def goodbye():
    "Print a farewell"
    print("Bye.")


# Main program begins here
dotwice(greeting)
dotwice(goodbye)
