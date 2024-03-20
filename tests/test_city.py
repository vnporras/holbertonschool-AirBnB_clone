#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.model = City()

    def tearDown(self):
        del self.model

    def daughterClass(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_atrr(self):
        my_city = self.model
        self.assertTrue(hasattr(my_city, "name"))
        self.assertTrue(hasattr(my_city, "state_id"))

    def test_to_dict(self):
        my_city = self.model
        my_city.name = "Cali"
        my_city.state_id = "Cra1a9bis73a23"
        my_model_json = my_city.to_dict()
        attrs = ["id",
                 "created_at",
                 "updated_at",
                 "name",
                 "state_id",
                 "__class__"]
        self.assertCountEqual(my_model_json.keys(), attrs)
        self.assertEqual(my_model_json['__class__'], 'City')
        self.assertEqual(my_model_json['name'], "Cali")
        self.assertEqual(my_model_json['state_id'], "Cra1a9bis73a23")

    def test_to_dict_values(self):
        format = "%Y-%m-%dT%H:%M:%S.%f"
        my_model = self.model
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["__class__"], "City")
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