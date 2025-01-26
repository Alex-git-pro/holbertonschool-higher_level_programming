#!/usr/bin/python3

"""
This module contains a function that prints a person's full name.

The `say_my_name` function takes a first name and a last name as arguments,
and prints the name in the format: "My name is <first_name> <last_name>".

If `first_name` or `last_name` is not a string a TypeError will be raised.

Example usage:
    say_my_name("John", "Doe")
    say_my_name("John")
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format: "My name is <first_name> <last_name>".

    Arguments:
    first_name -- The first name of the person.
    last_name -- The last name of the person (default is an empty string).

    If `first_name` or `last_name` is not a string, a TypeError will be raised.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}".strip())
