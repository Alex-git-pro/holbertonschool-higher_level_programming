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
        if attrs is None:
            return self.__dict__
        
        return {key: value for key, value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """Replace the attributes of the student with values from the dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
