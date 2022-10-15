#!/usr/bin/python3
"""
Module revie.py
contain:
    Class Revie inherits from Class BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel
    Public class attributes: place_id
    Public class attributes: user_id
    Public class attributes: text
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
