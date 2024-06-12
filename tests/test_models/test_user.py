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


class TestUser(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
