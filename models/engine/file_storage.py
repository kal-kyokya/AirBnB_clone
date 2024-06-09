#!/usr/bin/python3
"""
'file_storage' Is a Class creating module.
"""
import json


class FileStorage():
    """Blueprint for all instances of type FileStorage"""

    def __init__(self):
        """Constructs/Initializes all Class instances"""
        self.__file_path = "file.json"
        self.__objects = {}

    @property
    def objects(self):
        """Getter for the private attribute 'objects'.

        Setter comes right after.
        """
        return self.__objects

    @objects.setter
    def objects(self):
        pass

    def all(self):
        """Returns a dictionary of all stored objects."""
        return self.objects

    def new(self, my_dict={}):
        """Adds an object to the store."""
        self.objects.update({f'my_dict[id]': my_dict})

    def save(self):
        """Serializes 'objects' into a JSON file."""
        with ("file.json", "w") as jfile:
            json.dump(self.objects, jfile)

    def reload(self):
        """Deserializes an JSON file to a string object."""
        try:
            with ("file.json", "r") as jfile:
                self.objects = json.load(jfile)
        except:
            pass
