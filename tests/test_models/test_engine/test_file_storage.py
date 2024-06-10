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
from models import storage


class TestFileStorage(unittest.TestCase):
    """Class of test methods assessing the FileStorage Class."""

    def test_init(self):
        """Checks that no private attribute is accessed remotely"""
        obj = FileStorage()

        with self.assertRaises(AttributeError):
            objects = obj.objects
            file_path = obj.file_path

    def test_method_new(self):
        """Enforces passing an object to the method 'new'."""
        pass

    def test_method_all(self):
        """Confirms return type of the generated output of 'all'."""
        obj = FileStorage()
        self.assertIsInstance(obj.all(), dict)


if "__name__" == "__main__":
    unitttest.main()
