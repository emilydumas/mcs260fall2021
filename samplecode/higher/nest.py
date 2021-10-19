"Example of higher-order function"
# MCS 260 Fall 2021 Lecture 24
# https://www.dumas.io/teaching/2021/fall/mcs260/slides/lecture24.html#/6


# This is the higher-order function
def nest(func, val, times):
    """
    Compose `func` with itself `times` times
    and apply to val
    """
    for i in range(times):
        val = func(val)  # Changes to val don't affect anything outside function!
    return val


# Auxillary functions below


def double(x):
    "return twice x"  # obvious docstrings, included to build the habit
    return 2 * x


def five_percent_more(x):
    "return 105% of x"
    return 1.05 * x


# Main program begins here
print("Start with 3, double 8 times:")
print(nest(double, 3, 8))

print("Start with 200, increase by 5% 20 times:")
print(nest(five_percent_more, 200, 20))
# In both of these cases, short formulas could perform the calculation.
# We do it with `nest` to demonstrate its capability.
