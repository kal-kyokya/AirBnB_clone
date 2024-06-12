#!/usr/bin/python3
"""
'amenity' is a Class creating module.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Collection of class Attributes required for instanciation of Amenity class.

    Parent class:
        BaseModel: Comprises of fields needed for creation of Amenity object.
    """

    name = ""
