#!/usr/bin/python3
"""
'file_storage' is a Class creation module.
"""
import json


class FileStorage():
    """Blueprint for all instances of the class FileStorage.

    Class Attributes:
        file_path: String representing the path to the JSON File.
        objects: Dictionary of dictionary objects to be stored.
    """

    __file_path = "file.json"
    __objects = {}

    def new(self, my_dict):
        """Adds a dictionary to the collection of dictionaries.

        Arg:
            my_dict: New dictionary of the collection.

        Return:
            Nothing.
        """
        if my_dict is not None:
            key = self.__class__.__name__ + "." + my_dict['id']
            self.objects.update({f"{key}": my_dict})

    def save(self):
        """Serializes a dict to JSON string and stores it in a JSON file."""
        with open("file.json", "w") as jfile:
            for key, value in self.objects.items():
                jvalue = {f"{key}": value}
                json.load(jvalue, jfile)

    def reload(self):
        """Provides FileStorage instances with previously stored data."""
        with open("file.json", "r") as jfile:
            jdata = json.load(jfile)
