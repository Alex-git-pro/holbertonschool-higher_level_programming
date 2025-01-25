#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format: "My name is <first_name> <last_name>".

    Arguments:
    first_name -- first name of the person
    last_name -- last name of the person (default is an empty string)

    If either `first_name` or `last_name` is not a string, raise a TypeError.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}".strip())
