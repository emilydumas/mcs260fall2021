# MCS 260 Fall 2021 Project 1 solution
# David Dumas

def mwdp(x):
    """For an integer x, return the integer mean
    of x and d**k where d is the largest decimal
    digit of x and k is the number of decimal digits
    of x.  This is the _mean with digit power_."""
    digits = [int(c) for c in str(x)]
    maxdigit = max(digits)
    numdigits = len(digits)
    return (x + maxdigit ** numdigits) // 2

n = int(input("Starting value: "))
sequence = [n] # terms of the MWDP sequence computed so far
loop_detected = False

for i in range(100):
    print(sequence[-1])
    if sequence[-1] in sequence[:-1]:
        # The last term also appeared somewhere else
        # which means we've found a "loop"
        loop_detected = True
        break
    next_term = mwdp(sequence[-1])
    sequence.append(next_term)

# We might end up here because 100 terms were printed
# OR because a loop was detected.  The value of the
# boolean loop_detected tells us which is the case.
if loop_detected:
    print("looped")
else:
    print("maxiter")