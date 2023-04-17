#!/usr/bin/python3
""" Initializes a variable storage to create a unique FileStorage
instance """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
