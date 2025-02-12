#!/usr/bin/python3
"""
This module defines a function to read and print a text file's content.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read from. Default is an empty string.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
