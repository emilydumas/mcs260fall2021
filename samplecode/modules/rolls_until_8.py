"""
Roll two six-sided dice repeatedly, until the sum
is equal to 8.  Print the number of rolls.
"""

import dice

n = 0
k = 0
while n != 8:
    a,b = dice.roll_dice(number=2,sides=6)
    n = a+b
    print("Rolled {} and {} for a sum of {}".format(a,b,n))
    k += 1

print("A sum of 8 was obtained after {} rolls".format(k))
