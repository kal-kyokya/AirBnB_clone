#!/usr/bin/python3
"""
'base_model' is a class creation module
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """Defines all common attributes/methods of subclasses to come."""

    def __init__(self, *args, **kwargs):
        """Constructs/Initializes Instances of class BaseModel.

        Args:
            id: Unique identifier of each class instance.
            created_at: Time at which init method is called.
            updated_at: Time at which object is saved in json file.
            (*args, **kwargs): Arbitrary optional arguments.
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        self.__dict__.update(
                            {f"{key}": datetime.fromisoformat(value)})
                    else:
                        self.__dict__.update({f"{key}": value})
        else:
            models.storage.new(self)

    def __str__(self):
        """Customizes the string representations of BaseModel instances"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Edits 'updated_at' attributes and store calling object details."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Generates dictionary representation of the calling Instance."""
        dct = self.__dict__.copy()
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        dct.update({'__class__': self.__class__.__name__})
        return dct
