#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = none
    __session = none

    def __init__(self):
        self.__engine = create_engine(
            )
