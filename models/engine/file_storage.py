#!/usr/bin/env python3
#convercion de diccionario a json.json
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorange:
    
    __file_path = "file.json"
    __objects = {} 
    
    classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
               "City": City, "Place": Place, "Review": Review, "State": State}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """new - sets in __objects the obj"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj
    
    def save(self):
        """save - writes an Object to a text file"""
        new_dict = {}
        with open(self.__file_path, 'w') as save:
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, save)
        
    def reload(self):
        """reload - deserializes the JSON file to __objects"""
        all_obj = {}
        if path.exists(self.__file_path):
            all_obj = self.read_json()
        for key, value in all_obj.items():
            self.__objects[key] = self.classes[value['__class__']](**value)
