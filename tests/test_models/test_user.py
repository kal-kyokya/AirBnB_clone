#!/usr/bin/python3
"""
'test_user' is a file testing script
"""
# Project structure
# AirBnb_clone/
# ├── models/
# │   └── user.py
# └── tests/
#     └── test_user.py

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser1(unittest.TestCase):
    """Collection of methods testing parts of the 'user.py' script."""

    def test_email_class_attributes(self):
        """Asserts the presence of the email class attributes."""
        obj = User()
        self.assertTrue(hasattr(obj, "email"))

    def test_password_class_attributes(self):
        """Asserts the presence of the password class attributes."""
        obj = User()
        self.assertTrue(hasattr(obj, "password"))

    def test_first_name_class_attributes(self):
        """Asserts the presence of the first_name class attributes."""
        obj = User()
        self.assertTrue(hasattr(obj, "first_name"))

    def test_last_name_class_attributes(self):
        """Asserts the presence of the last_name class attributes."""
        obj = User()
        self.assertTrue(hasattr(obj, "last_name"))


class TestUser2(unittest.TestCase):
    """Test cases against the User class"""

    def test_attrs_are_class_attrs(self):
        u = User()
        # test that it is a class attribute
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))

    def test_class_attrs(self):
        u = User()
        self.assertIs(type(u.first_name), str)
        self.assertIs(type(u.last_name), str)
        self.assertTrue(u.first_name == "")
        self.assertTrue(u.last_name == "")

    def test_user_is_a_subclass_of_basemodel(self):
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))
if __name__ == "__main__":
    unittest.main()
