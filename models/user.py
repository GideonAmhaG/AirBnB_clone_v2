#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class User(BaseModel):
    """This class defines a user by various attributes"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'users'

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """
        init Function Docstring

        Initialize parent class (BaseModel)

        """
        super().__init__(*args, **kwargs)
