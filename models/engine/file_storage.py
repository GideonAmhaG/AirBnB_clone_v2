#!/usr/bin/python3
""" Module for FileStorage class """
from models.base_model import BaseModel
import json
from os import path
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """ serializes instances to a JSON file and deserializes JSON file to
    instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """  sets in __objects the obj with key <obj class name>.id """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """ deserializes the JSON file to __objects """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                json_dict = json.loads(f.read())
                for key, value in json_dict.items():
                    self.__objects[key] = eval(value["__class__"])(**value)

    def reset(self):
        """ resets all objects in __objects """
        self.__objects = {}
