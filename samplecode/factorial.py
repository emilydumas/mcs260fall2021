"""
Factorial as an example of recursion
"""
# MCS 260 Fall 2021 Lecture 29

# Convention:  0! = 1

def fact(n):
    """Return the factorial of n"""
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)

def fact_iterative(n):
    """Return the factorial of n"""
    f = 1
    for i in range(2,n+1): # i starts at 2 and ends at n
        f *= i
    return f

if __name__=="__main__":
    print("Factorials of integers 0 to 9 computed recursively and iteratively:")
    print(" n | rec n! | itr n!")
    for i in range(10):
        print("{:2d} {:8d} {:8d}".format(i,fact(i),fact_iterative(i)))
