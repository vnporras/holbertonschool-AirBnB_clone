#!/usr/bin/python3
""" File Storage Module """
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(self):
        return self.__objects

    @classmethod
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        objs = {}
        for key, obj in self.__objects.items():
            objs[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(objs, file)
            file.close()

    def reload(self):
        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place
        from ..review import Review

        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for key, value in json.load(file).items():
                    obj = eval(value["__class__"])(**value)
                    self.__objects[key] = obj
                    file.close()
        except FileNotFoundError:
            pass