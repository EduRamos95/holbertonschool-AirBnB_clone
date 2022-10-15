#!/usr/bin/python3
"""
mass module place.py
contain:
    Class coty  inherits from Class BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    city place inherits from BaseModel
    Public class attributes: city_id
    Public class attributes: user_id
    Public class attributes: name
    Public class attributes: description
    Public class attributes: number_rooms
    Public class attributes: number_bathrooms
    Public class attributes: max_guest
    Public class attributes: price_by_night
    Public class attributes: latitude
    Public class attributes: longitude
    Public class attributes: amenity_ids

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
