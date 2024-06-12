#!/usr/bin/python3
"""
'place' is a Class creation module.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Collection of class Attributes required for instanciation of Place class.

    Parent class:
        BaseModel: Comprises of fields needed for creation of Place object.
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
    amenity_ids = ""
