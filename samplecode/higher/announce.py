"Example of higher-order functions"
# MCS 260 Fall 2021 Lecture 24
import time


# This is the higher-order function
def announce_call(f, *args):
    """
    Print a message, call f with the given args,
    then print another message.
    """
    print("I am about to call the function")
    f(*args)
    print("I just finished calling the function")


# Auxillary functions below


def pause5():
    "Pauses for 5 seconds"
    time.sleep(5)


# Main program
announce_call(print)
announce_call(pause5)
announce_call(print, "The high temperature today was", 70, "degrees F.")
