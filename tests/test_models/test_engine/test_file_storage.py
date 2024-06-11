#!/usr/bin/python3
"""
'test_file_storage.py' is a Class testing file
"""
# Project structure
# AirBnb_clone/
# ├── models/
# │   ├── base_models.py
# │   ├── __init__.py
# │   └── engine/
# │       └── test_base_model.py
# └── tests/
#     ├── test_base_model.py
#     ├── test_file_storage.py
#     └── __init__.py
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models
import json


class TestFileStorageInit(unittest.TestCase):
    """Class of test methods assessing the FileStorage Class's Init method."""

    def test_init(self):
        """Checks that no private attribute is accessed remotely"""
        obj = FileStorage()

        with self.assertRaises(AttributeError):
            objects = obj.objects
            file_path = obj.file_path


class TestFileStorageMethods(unittest.TestCase):
    """Class of test methods assessing the FileStorage Class's methods."""

    def test_new_method(self):
        """Enforces passing an object to the method 'new'."""
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel." + obj.id, models.storage.all().keys())

    def test_all_method(self):
        """Confirms return type of the generated output of 'all'."""
        obj = FileStorage()
        self.assertEqual(type(obj.all()), dict)
        self.assertTrue(type(obj.all()) is dict)

    def test_save_method(self):
        """Asserts the existence of a stored/saved object post encoding."""
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        with open("file.json", "r") as jfile:
            data = json.load(jfile)
            self.assertIn("BaseModel." + obj.id, data)

    def test_reload_method(self):
        """Investigates the presence of a stored/saved object post decoding."""
#        obj = BaseModel()
#        models.storage.save()
#        models.storage.reload()
#        objects = FileStorage._FileStorage__objects
#        self.assertIn("BaseModel." + obj.id, objects)
#
#       with self.assertRaises(TypeError):
#            models.storage.reload(None)


if "__name__" == "__main__":
    unitttest.main()
