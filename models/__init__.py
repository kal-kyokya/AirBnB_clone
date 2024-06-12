#!/usr/bin/python3
"""
'__init__' Provides the models module with a instance of FileStorage.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
