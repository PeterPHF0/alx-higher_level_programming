#!/usr/bin/python3
"""Defines a name-printing function"""

def say_my_name(first_name, last_name=""):
    '''Print the name

    Args:
        first_name (str): first name
        last_name (str, optional): last name. Defaults to "".

    Raises:
        TypeError: If either of first_name or last_name are not strings.
    '''
    
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    
    elif type(last_name) != str:
        raise TypeError('last_name must be a string')
    
    print(f"My name is {first_name} {last_name}")
