#!/usr/bin/python3
"""State Module for HBNB project"""
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects"""
            all_cities = models.storage.all("City")
            city_list = []
            for c_id in all_cities:
                if all_cities[c_id].state_id == self.id:
                    city_list.append(all_cities[c_id])

            return city_list
