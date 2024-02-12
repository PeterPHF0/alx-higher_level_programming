#!/usr/bin/python3
"""Defines an integer addition function"""

def add_integer(a, b=98):
    """Return the result of adding its 2 integer aruguments

    Floating points numbers are type casted to int before addition

    Raises:
        TypeError if either a or b is a non-integer and non-float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
