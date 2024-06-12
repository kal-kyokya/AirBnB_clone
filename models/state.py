#!/usr/bin/python3
"""
'state' is a Class creating module.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Collection of class Attribute(s) required for instanciation of State class.

    Parent class:
        BaseModel: Comprises of fields needed for creation of state object.
    """

    name = ""
