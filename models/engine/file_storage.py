#!/usr/bin/python3
"""
'file_storage' is a Class creation module.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """Blueprint for all instances of the class FileStorage.

    Class Attributes:
        file_path: String representing the path to the JSON File.
        objects: Dictionary of BaseModel objects to be stored.
    """

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Adds a class object to the '__objects' dictionary.

        Arg:
            obj: New instance added to the dictionary.

        Return:
            Nothing.
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes a dict to JSON string and stores it in a JSON file."""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as jfile:
            json.dump(json_objects, jfile)

    def reload(self):
        """Provides FileStorage instances with previously stored data."""
        try:
            with open(self.__file_path, "r") as jfile:
                data = json.load(jfile)
                for key, value in data.items():
                    class_name = value['__class__']
                    del value['__class__']
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass

    def all(self):
        """Returns the dictionary containing all objects saved in the past."""
        return (self.__objects)
