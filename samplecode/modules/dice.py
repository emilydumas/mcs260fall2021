"""
Functions related to rolling dice
"""
# MCS 260 Fall 2021 Lecture 23

import random

def roll_die(sides=6):
    """
    Roll a single die with `sides` sides numbered
    1, 2, ..., `sides` and return the resule (an
    integer).
    """
    return random.randint(1,sides)

def roll_dice(number,sides=6):
    """
    Roll `number` dice, each having `sides` sides.
    Return a list of the rolls.
    """
    return [ roll_die(sides=sides) for i in range(number) ]

#            roll_die(sides=12)
# Let's imagine I called roll_dice(2,12)


def flip_coin():
    """
    Returns one of the strings "heads" or "tails", each
    equally likely.
    """
    return random.choice( ["heads","tails"] )

#print("Thank you for importing the dice module.")
#print("I hope that you have a nice day.")