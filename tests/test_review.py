#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestUser(unittest.TestCase):
    def setUp(self):
        self.model = Review()

    def tearDown(self):
        del self.model

    def daughterClass(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_atrr(self):
        my_review = self.model
        self.assertTrue(hasattr(my_review, "place_id"))
        self.assertTrue(hasattr(my_review, "user_id"))
        self.assertTrue(hasattr(my_review, "text"))

    def test_to_dict(self):
        my_review = self.model
        my_review.place_id = "***a"
        my_review.user_id = "*****123"
        my_review.text = "Brayan"
        my_model_json = my_review.to_dict()
        attrs = ["id",
                 "created_at",
                 "updated_at",
                 "place_id",
                 "user_id",
                 "text",
                 "__class__"]
        self.assertCountEqual(my_model_json.keys(), attrs)
        self.assertEqual(my_model_json['__class__'], 'Review')
        self.assertEqual(my_model_json['place_id'], "***a")
        self.assertEqual(my_model_json['user_id'], "*****123")
        self.assertEqual(my_model_json['text'], "Brayan")

    def test_to_dict_values(self):
        format = "%Y-%m-%dT%H:%M:%S.%f"
        my_model = self.model
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["__class__"], "Review")
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