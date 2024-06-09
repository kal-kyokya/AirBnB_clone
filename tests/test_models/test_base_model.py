#!/usr/bin/python3
"""
'test_base_model' is the unit test for /models/base_model.py
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Collection of test methods for the base model module.

    Parent Class:
        TestCase: Provides methods for assertion and testing.
    """

    def test_Object_Attr(self):
        """Runs tests on Instance Attributes of BaseModel"""
        obj = BaseModel()
        self.assertEqual(type(obj.id), type(uuid.uuid4()))
        self.assertEqual(type(obj.created_at), type(datetime.now()))
        self.assertEqual(type(obj.updated_at), type(datetime.now()))

    def test_str(self):
        """Assert compliance of 'dunder str' representation to requierment"""
        obj = BaseModel()
        self.assertEqual(
            str(obj),
            f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}")

    def test_save(self):
        """Confirms that saving action is done sucessffully."""
        obj = BaseModel()
        before = obj.updated_at
        after = obj.save()
        self.assertNotEqual(before, after)

    def test_to_dict(self):
        """Tests the conversion tool 'to_dict'."""
        obj = BaseModel()
        my_dict = obj.__dict__.copy()
        my_dict.update({"__class__": obj.__class__.__name__})
        my_dict['created_at'] = obj.created_at.isoformat()
        my_dict['updated_at'] = obj.updated_at.isoformat()
        dct = obj.to_dict()
        self.assertEqual(my_dict, dct)


if __name__ == "__main__":
    unittest.main()
