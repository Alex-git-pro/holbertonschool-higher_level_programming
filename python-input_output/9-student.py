#!/usr/bin/python3
"""Module for reading a text file"""


class Student:
    """Class representing a student."""
    
    def __init__(self, first_name, last_name, age):
        """Initialize a new student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary representation of the student instance."""
        return self.__dict__
