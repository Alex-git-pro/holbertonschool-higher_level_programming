#!/usr/bin/python3

def class_to_json(obj):
    """Return the dictionary description with simple data structure for JSON serialization."""
    return obj.__dict__
