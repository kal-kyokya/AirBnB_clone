#!/usr/bin/python3
"""
'city' is a Class creation module.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Collection of class Attributes required for instanciation of City class.

    Parent class:
        BaseModel: Comprises of fields needed for creation of City object.
    """

    state_id = ""
    name = ""
