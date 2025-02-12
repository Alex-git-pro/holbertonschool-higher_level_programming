#!/usr/bin/python3
"""Module for reading a text file"""


import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    
    Args:
        my_obj (any): The Python object to convert to JSON string.
        
    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
