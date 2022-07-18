#!/usr/bin/env python3
# convercion de diccionario a json.json
import json
import os
import os.path as path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review



class FileStorage:
    """filestorage class"""
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
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        list_className = {
            "BaseModel": BaseModel, "User": User,
            "State": State, "City": City,
            "Amenity": Amenity, "Place": Place,
            "Review": Review}
        new_dic = {}
        name_class = ""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file_json:
                new_dic = json.load(file_json)
                for key, obj in new_dic.items():
                    name_class = self.parse(key)
                    new_obj = list_className[name_class](**obj)
                    new_dic[key] = new_obj
                self.__objects = new_dic
        else:
            pass
