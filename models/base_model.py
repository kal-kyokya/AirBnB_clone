#!/usr/bin/python3
"""
'base_model' is a class creation module
"""
import uuid
from datetime import datetime


class BaseModel():
    """Defines all common attributes/methods of subclasses to come."""

    def __init__(self, *args, **kwargs):
        """Constructs/Initializes Instances of class BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != "__class__":
                    self.key = value
                    self.__dict__.update({f"{key}": value})

    def __str__(self):
        """Customizes the string representations of BaseModel instances"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Passes time at which method is called to 'updated_at'"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Generates dictionary representation of the BaseModel Instance."""
        dct = self.__dict__.copy()
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        dct.update({'__class__': self.__class__.__name__})
        return dct
