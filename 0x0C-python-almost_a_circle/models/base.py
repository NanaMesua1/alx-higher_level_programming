#!/usr/bin/python3
"""base
"""
import json
import csv
class Base:
    """Base of the other shapes
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
