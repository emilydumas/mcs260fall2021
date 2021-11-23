"""Password generation algorithms"""
# MCS 260 Fall 2021
# David Dumas
import random

# Password character classes
LCL = "abcdefghijklmnopqrstuvwxyz"
UCL = LCL.upper()
SYMB = "!@#$%^&*()-+=_"
DIGIT = "0123456789"

def random_password(length=8,
                    special_frac=0.5,
                    require_capital=False,
                    require_symbol=False,
                    require_digit=False):
    """
    Generate a random password of length `length`, in which the
    fraction `special_frac` consists of characters other than 
    lowercase letters.  The character classes available for these
    other characters are controlled by the flags:
      `require_capital` : Capital letters (A-Z)
      `require_symbol` : Symbols (!@#$%^&*()-+=_)
      `require_digit` : Digits (0-9)
    Each of these flags also adds a requirement that at least
    one character from that class must be present.

    If all the `require_*` flags are False, then `special_frac`
    is ignored and a random password of lowercase letters is
    returned.
    """

    if not any([require_capital, require_symbol, require_digit]):
        return "".join([random.choice(LCL) for _ in range(length)])

    # How many characters are claimed by the minimum required elements?
    n_fixed = 0
    for f in [require_capital, require_symbol, require_digit]:
        if f:
            n_fixed += 1
    # Does the requested length make it impossible to satisfy the
    # requirements?
    if length < n_fixed:
        raise ValueError("Length too small to include all required elements")
    
    # Decide how many non-lowercase ("special") characters to have
    n_spec = max(int(special_frac*length), n_fixed)
    # How many lowercase letters will be in the password
    n_letter = length - n_spec

    # A list of alphabets available for special characters
    spec_choices = []
    if require_capital:
        spec_choices.append(UCL)
    if require_symbol:
        spec_choices.append(SYMB)
    if require_digit:
        spec_choices.append(DIGIT)

    # Allocate special characters to the various classes by
    # choosing an alphabet for each one
    spec_options = [ random.choice(spec_choices) for _ in range(n_spec) ]
    
    # Fix the allocation so it always meets the required elements
    i = 0
    if require_capital:
        spec_options[i] = UCL
        i += 1
    if require_symbol:
        spec_options[i] = SYMB
        i += 1
    if require_digit:
        spec_options[i] = DIGIT
    
    # Choose the special chars from their respective alphabets
    specs = [ random.choice(x) for x in spec_options ]

    # Choose the lower case letters we will include
    letters = [ random.choice(LCL) for _ in range(n_letter) ]

    # Assemble in random order
    L = specs+letters
    random.shuffle(L)

    # Join and return
    return "".join(L)
