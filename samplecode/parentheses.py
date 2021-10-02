"""Detect matching of parentheses in an expression"""
# MCS 260 Fall 2021 Lecture 17

# Read expression (which should include parentheses)
s = input("Expression: ")

# We'll use a stack to keep track of all the "("
# that haven't been matched with ")" yet.  Every
# new "(" we see gets pushed, and every ")" we see
# closes whatever is at the top of the stack.
currently_open = []

# We want both the characters of s and their positions
# so we use enumerate()
for i,c in enumerate(s):
    # c is character from s
    # i is the position (0-based index) of that character in s
    if c == "(":
        # New left paren opened; push it
        currently_open.append(i)
    elif c == ")":
        # Right paren closes whatever left paren is at the
        # top of the stack.  But we need to make sure the 
        # stack is nonempty before trying to pop.
        if len(currently_open) > 0:
            # Ok
            currently_open.pop()
        else:
            # Error because there was no "(" on the
            # stack to match this ")"
            print("Error:")
            print(s)
            print(" "*i + "^ does not match any preceding (")
            exit()
    
# are there any parentheses open?
# If so, it means that there is a ( with no match
if len(currently_open) > 0:
    print("Error:")
    print(s)
    print(" "*currently_open.pop() + "^ is not matched by any following )")
else:
    print("Parentheses matched successfully.")

# Examples of what we expect the error messages to look like:

# (1 + ((2+3) - 5
#      ^  is not matched by any following )

# ( 1 + (3-4))) + 5
#             ^ does not match any preceding (