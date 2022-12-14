#!/usr/bin/python3
"""
Module Amenity.py
contain:
    Class Amenity inherits from Class BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    amenity: inherits from BaseModel
    Public class attributes: Name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
