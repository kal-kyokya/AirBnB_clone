#!/usr/bin/python3
"""
'review' is a Class creation module.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Collection of class Attributes required for instanciation of Review class.

    Parent class:
        BaseModel: Comprises of fields needed for creation of Review object.
    """

    place_id = ""
    user_id = ""
    text = ""
