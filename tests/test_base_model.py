#!/usr/bin/python3
import unittest
from unittest import mock
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def tearDown(self):
        del self.model

    def test_atrributes(self):
        self.model.name = "Brayan"
        self.model.age = 21
        self.assertEqual(self.model.name, "Brayan")
        self.assertEqual(self.model.age, 21)

    def test_str(self):
        class_name = self.model.__class__.__name__
        output = f"[{class_name}] ({self.model.id}) {str(self.model.__dict__)}"
        self.assertEqual(output, self.model.__str__())

    def test_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        attrs = ["id",
                 "created_at",
                 "updated_at",
                 "name",
                 "my_number",
                 "__class__"]
        self.assertCountEqual(my_model_json.keys(), attrs)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)

    def test_to_dict_values(self):
        format = "%Y-%m-%dT%H:%M:%S.%f"
        my_model = self.model
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["__class__"], "BaseModel")
        self.assertEqual(type(my_model_json["created_at"]), str)
        self.assertEqual(type(my_model_json["updated_at"]), str)
        self.assertNotEqual(my_model_json["created_at"],
                            my_model.created_at)
        self.assertNotEqual(my_model_json["updated_at"],
                            my_model.updated_at)

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        instance = self.model
        prev_created_at = instance.created_at
        prev_updated_at = instance.updated_at
        instance.save()
        new_created_at = instance.created_at
        new_updated_at = instance.updated_at
        self.assertNotEqual(prev_updated_at, new_updated_at)
        self.assertEqual(prev_created_at, new_created_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)