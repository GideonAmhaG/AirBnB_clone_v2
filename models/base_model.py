#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    """
    BaseModel Class Docstring

    Defines all common attributes/methods for other classes
    """
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        init Function Docstring

        Class Constructor
        id: string - assignes a unique uuid when an\
        instance is created
        created_at: datetime - assign with the current\
        datetime when an instance is created
        updated_at: datetime - assign with the current\
        datetime when an instance is created and it will\
        be updated every time you change
        """

        if kwargs:
            id_exists = 0
            created_at_exists = 0
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        if key == "created_at":
                            created_at_exists = 1
                        if not isinstance(value, datetime):
                            value = datetime.strptime(
                                                    value,
                                                    '%Y-%m-%dT%H:%M:%S.%f')
                    if key == 'id':
                        id_exists = 1
                    setattr(self, key, value)
            if id_exists == 0:
                self.id = str(uuid.uuid4())
            if created_at_exists == 0:
                self.created_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
        self.save()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """
        save Function Docstring

        Return: Updates the public instance attribute\
        updated_at with the current datetime
        """
        self.__dict__["updated_at"] = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
