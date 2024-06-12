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

    def test_class_attributes(self):
        """Asserts the presence of a set of class attributes."""
        obj = User()
        self.assertTrue(hasattr(obj, "email"))
        self.assertTrue(hasattr(obj, "password"))
        self.assertTrue(hasattr(obj, "first_name"))
        self.assertTrue(hasattr(obj, "last_name"))


if __name__ == "__main__":
    unittest.main()
