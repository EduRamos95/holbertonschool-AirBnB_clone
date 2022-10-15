#!/usr/bin/python3
"""
Module city.py
contain:
    Class City inherits from Class BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ city class inherits from BaseModel
     Public class attributes: state_id
      Public class attributes: Name
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes City"""
        super().__init__(*args, **kwargs)
