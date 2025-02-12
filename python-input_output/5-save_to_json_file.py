#!/usr/bin/python3
"""Module for reading a text file"""


import json

def save_to_json_file(my_obj, filename):
    """Saves an object to a file as a JSON string"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
