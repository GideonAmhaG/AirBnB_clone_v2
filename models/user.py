#!/usr/bin/python3
""" module for USer class """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from os import getenv
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """ a class User that inherits from BaseModel """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship(
            'Place',
            cascade="all, delete, delete-orphan",
            backref='user')
        reviews = relationship(
            'Review',
            cascade="all, delete, delete-orphan",
            backref='user'
        )
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        places = None
        reviews = None

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)
