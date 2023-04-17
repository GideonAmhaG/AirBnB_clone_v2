#!/usr/bin/python3
""" module for USer class """
from models.base_model import BaseModel


class User(BaseModel):
    """ a class User that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
