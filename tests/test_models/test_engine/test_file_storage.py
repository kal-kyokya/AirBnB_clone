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


class TestFileStorage(unittest.TestCase):
    """Class of test methods assessing the FileStorage Class."""

    def test_init(self):
        """Checks that no private attribute is accessed remotely"""
        obj = FileStorage()

        with self.assertRaises(AttributeError):
            objects = obj.objects
            file_path = obj.file_path

    def test_new_method(self):
        """Enforces passing an object to the method 'new'."""
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel." + obj.id, models.storage.all().keys())

    def test_all_method(self):
        """Confirms return type of the generated output of 'all'."""
        obj = FileStorage()
        self.assertIsInstance(obj.all(), dict)

    def test_save_method(self):
        """Asserts the existance of a stored/saved object."""
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertNotEqual(models.storage.all(), None)


if "__name__" == "__main__":
    unitttest.main()
