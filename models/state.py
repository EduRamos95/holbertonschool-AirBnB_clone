#!/usr/bin/python3
"""
Module state
contain:
    Class State inherits from Class BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State: inherits from BaseModel
    Public class attributes: Name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes State"""
        super().__init__(*args, **kwargs)
