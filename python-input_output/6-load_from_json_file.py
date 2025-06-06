#!/usr/bin/python3
"""Module for reading a text file"""


import json

def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
