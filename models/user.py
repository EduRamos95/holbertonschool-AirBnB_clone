#!/usr/bin/python3
"""
Module user
contain:
    Class User inherits from Class BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User: inherits from BaseModel
    Public class attributes:
        email        password
        first_name   last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ initializes user instance """
        super().__init__(*args, **kwargs)
