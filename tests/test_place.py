#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestUser(unittest.TestCase):
    def setUp(self):
        self.model = Place()

    def tearDown(self):
        del self.model

    def daughterClass(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_atrr(self):
        my_place = self.model
        self.assertTrue(hasattr(my_place, "city_id"))
        self.assertTrue(hasattr(my_place, "user_id"))
        self.assertTrue(hasattr(my_place, "name"))
        self.assertTrue(hasattr(my_place, "description"))

    def test_to_dict(self):
        my_place = self.model
        my_place.city_id = "Cali"
        my_place.user_id = "***123"
        my_place.name = "Zonamerica"
        my_place.description = "Hi"
        my_model_json = my_place.to_dict()
        attrs = ["id",
                 "created_at",
                 "updated_at",
                 "city_id",
                 "user_id",
                 "name",
                 "description",
                 "__class__"]
        self.assertCountEqual(my_model_json.keys(), attrs)
        self.assertEqual(my_model_json['__class__'], 'Place')
        self.assertEqual(my_model_json['city_id'], "Cali")
        self.assertEqual(my_model_json['user_id'], "***123")
        self.assertEqual(my_model_json['name'], "Zonamerica")
        self.assertEqual(my_model_json['description'], "Hi")

    def test_to_dict_values(self):
        format = "%Y-%m-%dT%H:%M:%S.%f"
        my_model = self.model
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["__class__"], "Place")
        self.assertEqual(type(my_model_json["created_at"]), str)
        self.assertEqual(type(my_model_json["updated_at"]), str)
        self.assertNotEqual(my_model_json["created_at"],
                            my_model.created_at)
        self.assertNotEqual(my_model_json["updated_at"],
                            my_model.updated_at)

    def test_str(self):
        class_name = self.model.__class__.__name__
        output = f"[{class_name}] ({self.model.id}) {str(self.model.__dict__)}"
        self.assertEqual(output, self.model.__str__())

    def test_save(self):
        prev_created_at = self.model.created_at
        prev_updated_at = self.model.updated_at
        self.model.save()
        now_created_at = self.model.created_at
        now_updated_at = self.model.updated_at
        self.assertNotEqual(prev_updated_at, now_updated_at)
        self.assertEqual(prev_created_at, now_created_at)