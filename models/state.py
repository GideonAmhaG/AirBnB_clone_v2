#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import models


class State(BaseModel):
    """ The State class, contains name """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            db_storage = models.storage.all('City').values()
            for i in db_storage:
                if self.id == i.state_id:
                    return i

        name = ""

    def __init__(self, *args, **kwargs):
        """
        init Function Docstring

        Initialize parent class (BaseModel)

        """
        super(State, self).__init__(*args, **kwargs)
