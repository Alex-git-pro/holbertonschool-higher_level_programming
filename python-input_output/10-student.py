#!/usr/bin/python3

class Student:
    """Class representing a student."""
    
    def __init__(self, first_name, last_name, age):
        """Initialize a new student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the student instance."""
        # If no attrs is given, return all attributes
        if attrs is None:
            return self.__dict__
        
        # Filter the attributes based on the provided list
        return {key: value for key, value in self.__dict__.items() if key in attrs}
