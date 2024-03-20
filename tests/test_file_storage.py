#!/usr/bin/python3
import unittest
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.state import State
from models.place import Place
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.model = FileStorage()

    def tearDown(self):
        del self.model

    def testFilePath(self):
        self.assertEqual(self.model._FileStorage__file_path, "file.json")

    def test_all(self):
        new_dict = self.model.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, self.model._FileStorage__objects)

    def test_new(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        key = f"{my_model.__class__.__name__}.{my_model.id}"
        self.assertIn(key, self.model._FileStorage__objects, "No exists")

    def test_save(self):
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        file_json = json.dumps(new_dict)
        with open("file.json", "r", encoding="utf-8") as file:
            file_read = file.read()
        self.assertEqual(json.loads(file_json), json.loads(file_read))