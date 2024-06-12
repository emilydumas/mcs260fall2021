"""
Functions to study the dynamics of a function of one integer
that returns an integer.

(Dynamics means the study of behavior when a function is applied
repeatedly.)
"""

# MCS 260 Fall 2021 Project 3 solution
# Emily Dumas

def orbit(f,x0,n):
    """
    Compute the first `n` terms of the orbit of `x0` under
    the function `f`.
    Arguments:
        `f` - a function (should take one integer argument and return an integer)
        `x0` - a value of the type that `f` accepts as its argument
        `n` - the number of points to compute (a positive integer)
    Returns:
        A list of length `n` containing the values [ x0, f(x0), f(f(x0)), f(f(f(x0))), ... ]
    """
    L = [x0]
    # Python lets you use `_` as a variable name, and the convention
    # is to use it when you need a variable name, but will never use
    # the value of that variable.  That's the case here; we need to 
    # do something `n-1` times, but don't care about the current
    # iteration number.
    for _ in range(n-1):
        L.append(f(L[-1]))
    return L

def orbit_data(f,x0):
    """
    Repeatedly apply function `f` to initial value `x0` until some
    value is seen twice.  Return dictionary of data about the observed
    behavior.

    Arguments:
        `f` - a function (should take one integer argument and return an integer)
        `x0` - a value of the type that `f` accepts as its argument

    Returns:
        Dictionary with the following keys (after each key is a description of
        the associated value):
           "initial": The part of the orbit up to, but not including, the first
                value that is ever repeated.
           "cycle": The part of the orbit between the first and second instances of
                the first value that appears twice, including the first but not the
                second.  In other words, the entire orbit consits of the "initial"
                part followed by the "cycle" repeating over and over again.

    Example: Suppose that applying f repeatedly to start value 11 gives this sequence:
    11, 31, 12, 5, 6, 2, 8, 19, 17, 8, 19, 17, 8, 19, 17, 8, ...

    Then the return value would be:
    {
        "initial":[11, 31, 12, 5, 6, 2],
        "cycle": [8,19,17]
    }
    
    (If the orbit of `x0` doesn't end up in a cycle, it's ok for this function to run forever
    trying to find one.)
    """
    L = [x0]
    d = dict()
    while True:
        y = f(L[-1])
        if y in L:
            i = L.index(y)
            return { 
                "initial": L[:i],
                "cycle": L[i:],
            }
        else:
            L.append(y)

def eventual_period(f,x0):
    """
    Determine the length of the periodic cycle that `x0` ends up in.
    
    Arguments:
        `f` - a function (should take one integer argument and return an integer)
        `x0` - a value of the type that `f` accepts as its argument

    Returns:
        The length of the periodic cycle that the orbit of `x0` ends up in.

    Example: Suppose that applying f repeatedly to start value 11 gives this sequence:
    11, 31, 12, 5, 6, 2, 8, 19, 17, 8, 19, 17, 8, 19, 17, 8, ...
    
    Then the return value of eventual_period(f,11) would be 3, since the periodic
    cycle contains the 3 values 8,19,17.
    
    (If the orbit of `x0` doesn't end up in a cycle, it's ok for this function to run forever
    trying to find one.)
    """
    return len(orbit_data(f,x0)["cycle"])
    
def steps_to_enter_cycle(f,x0):
    """
    Determine the length of the intial part of the orbit of `x0` under `f` before
    it enters a periodic cycle.
    
    Arguments:
        `f` - a function (should take one integer argument and return an integer)
        `x0` - a value of the type that `f` accepts as its argument

    Returns:
        The number of elements of the orbit of `f` before the first value that 
        repeats.
        
    Example: Suppose that applying f repeatedly to start value 11 gives this sequence:
    11, 31, 12, 5, 6, 2, 8, 19, 17, 8, 19, 17, 8, 19, 17, 8, ...
    
    Then the return value of steps_to_enter_cycle(f,11) would be 6, because there are 6
    values in the intial segment of the orbit (i.e. 11, 31, 12, 5, 6, 2) which are followed by
    a periodic cycle.
    
    (If the orbit of `x0` doesn't end up in a cycle, it's ok for this function to run forever
    trying to find one.)
    """
    return len(orbit_data(f,x0)["initial"])

def eventual_cycle(f,x0):
    """
    Return the periodic cycle that the orbit of x0 ends up in as a list.
    
    Arguments:
        `f` - a function (should take one integer argument and return an integer)
        `x0` - a value of the type that `f` accepts as its argument

    Returns:
        The earliest segment from the orbit of `x0` under `f` that repeats
        indefinitely thereafter, as a list.
        
    Example: Suppose that applying f repeatedly to start value 11 gives this sequence:
    11, 31, 12, 5, 6, 2, 8, 19, 17, 8, 19, 17, 8, 19, 17, 8, ...
    
    Then eventual_cycle(f,x0) would return [8, 19, 17].
    
    (If the orbit of `x0` doesn't end up in a cycle, it's ok for this function to run forever
    trying to find one.)
    """
    return orbit_data(f,x0)["cycle"]    
    
def smallest_first(L):
    """
    Rotates a list so that its smallest element appears first.
    
    Arguments:
       `L`: A list of integers, no two of them equal
       
    Returns:
       A list that is the result of moving the first element of `L` to the end,
       repeatedly, until the first element of `L` is the smallest element of the list.
       
    Example: smallest_first([46,41,28]) returns [28,46,41]
    Example: smallest_first([4,2,1]) returns [1,4,2]
    Example: smallest_first([9,8,7,6,5,4,3,2,1]) returns [1,9,8,7,6,5,4,3,2]
    """
    i = L.index(min(L))
    return L[i:] + L[:i] # min and after, then things before the min

def find_cycles(f,start_vals):
    """
    Find all the periodic cycles of the function `f` that appear when you consider
    orbits of the elements of `start_vals`.
    
    Arguments:
        `f` - a function (should take one integer argument and return an integer)
        `start_vals` - a list of integers to use as starting values

    Returns:
        A list of lists, consisting of all the periodic cycles that are seen
        in the orbits of the start values from `start_vals`.  Each cycle is 
        given with its smallest entry appearing first, and any given cycle
        appears only once in the list.
       
    e.g. If `mwdp` is the mean with digit power function, then find_cycles(mwdp,[65,66,67])
    would return [ [28,46,41], [38,51] ] because both 65 and 67 end up in the [28,46,41]
    cycle and 66 ends up in the [38,51] cycle.
    """
    cycles = []
    for x0 in start_vals:
        c = smallest_first(eventual_cycle(f,x0))
        if c not in cycles:
            cycles.append(c)
    return cycles