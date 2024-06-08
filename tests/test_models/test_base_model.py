#!/usr/bin/python3
"""
'test_base_model' is the unit test for /models/base_model.py
"""
import unittest
from models import base_model
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Collection of test methods for the base model module.

    Parent Class:
        TestCase: Provides methods for assertion and testing.
    """

    def setUp(self):
        """Methods that runs before each individual test."""
        pass

    def test_Object_Attr(self):
        """Runs tests on Instance Attributes of BaseModel"""
        self.assertIsInstance(self.id, uuid.UUID)
        self.assertIsInstance(self.created_at, datetime.datetime)
        self.assertIsInstance(self.updated_at, datetime.datetime)

    def test_str(self):
        """Assert compliance of 'dunder str' representation to requierment"""
        str_list = str(self).split()
        my_list = [f"[{self.__class_.__name__}]",
                   f"({self.id})", f"{self.__dict__}"]
        count = 0
        for element in my_list:
            self.assertEqual(element, str_list[count])
            count += 1

    def test_save(self):
        """Confirms that saving action is done sucessffully."""
        before = self.updated_at
        after = self.save()
        self.assertNotEqual(before, after)

    def test_to_dict(self):
        """Tests the conversion tool 'to_dict'."""
        my_dict = self.__dict__.copy()
        my_dict.update({"__class__": self.__class__.__name__})
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        dct = self.to_dict()
        self.assertEqual(my_dict, dct)


if __name__ == "__main__":
    unittest.main()
