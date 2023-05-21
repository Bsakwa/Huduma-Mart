#!/usr/bin/python3

"""
Unittest for BaseModel class
"""

import models
from datetime import datetime
import unittest
from models.base_model import BaseModel


class BaseModelTests(unittest.TestCase):

    def setUp(self):
        """
        Create a new instance of BaseModel before each test
        """
        self.base_model = BaseModel()

    def test_id_is_string(self):
        """
        Test that BaseModel.id is a string
        """
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """
        Test that BaseModel.created_at is a datetime
        """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test that BaseModel.updated_at is a datetime
        """
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        Test that BaseModel.save() updates the updated_at attribute
        """
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict_returns_dictionary(self):
        """
        Test that BaseModel.to_dict() returns a dictionary
        """
        dictionary = self.base_model.to_dict()
        self.assertIsInstance(dictionary, dict)

    def test_to_dict_includes_classname(self):
        """
        Test that BaseModel.to_dict() includes the class name
        """
        dictionary = self.base_model.to_dict()
        self.assertIn('__class__', dictionary)

    def test_to_dict_excludes_private_attributes(self):
        """
        Test that BaseModel.to_dict() doesn't include private attributes
        """
        dictionary = self.base_model.to_dict()
        self.assertNotIn('_sa_instance_state', dictionary)

    def test_delete_removes_instance_from_storage(self):
        """
        Test that BaseModel.delete() removes an instance from storage
        """
        self.base_model.save()
        model_id = self.base_model.id
        self.base_model.delete()
        self.assertIsNone(models.storage.get_by_id(model_id))

    def test_str_representation(self):
        """
        Test that BaseModel.__str__ is a string representation of the BaseModel
        """
        string = str(self.base_model)
        self.assertEqual(string,
                         "[BaseModel] ({}) {}".format(self.base_model.id,
                                                      self.base_model.__dict__))

    def test_custom_attributes(self):
        """
        Test that custom attributes can be added to BaseModel
        """
        base_model = BaseModel(name="Test", age=25)
        self.assertEqual(base_model.name, "Test")
        self.assertEqual(base_model.age, 25)

    def test_custom_attributes_to_dict(self):
        """
        Test that custom attributes are included in the dictionary representation
        """
        base_model = BaseModel(name="Test", age=25)
        dictionary = base_model.to_dict()
        self.assertEqual(dictionary['name'], "Test")
        self.assertEqual(dictionary['age'], 25)

    def test_custom_attributes_str_representation(self):
        """
        Test that custom attributes are included in the string representation
        """
        base_model = BaseModel(name="Test", age=25)
        string = str(base_model)
        self.assertEqual(string,
                         "[BaseModel] ({}) {}".format(base_model.id,
                                                      base_model.__dict__))

    def test_custom_attributes_save_and_reload(self):
        """
        Test that custom attributes are saved and reloaded correctly
        """
        self.base_model.name = "Test Model"
        self.base_model.value = 10
        self.base_model.save()
        model_id = self.base_model.id
        reloaded_model = models.storage.get(BaseModel, model_id)
        self.assertIsNotNone(reloaded_model)
        self.assertEqual(reloaded_model.name, "Test Model")
        self.assertEqual(reloaded_model.value, 10)


    def test_delete_removes_instance_from_storage(self):
        """
        Test that BaseModel.delete() removes an instance from storage
        """
        self.base_model.save()
        model_id = self.base_model.id
        self.base_model.delete()
        retrieved_model = models.storage.get(BaseModel, model_id)
        self.assertIsNone(retrieved_model)


if __name__ == '__main__':
    unittest.main()
