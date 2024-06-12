#!/usr/bin/python3
"""
'user' is a Class creation module.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Collection of class Attributes required for instanciation of User class.

    Parent class:
        BaseModel: Comprises of fields needed for creation of User object.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
