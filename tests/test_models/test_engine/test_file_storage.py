#!/usr/bin/python3

"""Unittest for our FileStorage class"""

import models
import unittest
import json
from models.engine import file_storage
from models.user import User
from models.service_provider import ServiceProvider
FileStorage = file_storage.FileStorage


class FileStorageTestCase(unittest.TestCase):
    def setUp(self):
        """
        Create an instance for our tests
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Perform a clean up after the tests
        """
        pass

    def test_all(self):
        """
        Test the 'all' method
        """

        # Create a new object
        user = User()
        self.storage.new(user)

        # Check if the object exists in the storage
        self.assertIn(user, self.storage.all().values())

    def test_new(self):
        """
        Test the 'new' method
        """

        # Create a new object
        user = User()
        self.storage.new(user)

        # Check if the object exists in the storage
        self.assertIn(user, self.storage.all().values())

    def test_save(self):
        """
        Test the 'save' method
        """
        # Create a new object
        user = User()
        self.storage.new(user)

        # Save the storage to the file
        self.storage.save()

        # Read the file to get the serialized object
        with open(self.storage._FileStorage__file_path, 'r') as f:
            serialized_objects = json.load(f)

        # Check if the serialized object is the same as the original object
        for obj in serialized_objects.values():
            if obj['id'] == user.id:
                self.assertEqual(obj, user.to_dict())

    def test_delete(self):
        """
        Test the 'delete' method
        """

        # Create an object and add it to the storage
        user = User()
        self.storage.new(user)

        # Delete the object from the storage
        self.storage.delete(user)

        # Check if the object is no longer in the storage
        self.assertNotIn(user.id, self.storage.all())

    def test_get(self):
        """
        Test the 'get' method
        """
        # Create an object and add it to the storage
        user = User()
        self.storage.new(user)

        # Get the object from the storage by class name and ID
        retrieved_user = self.storage.get(User, user.id)

        # Check if the retrieved object is the same as the original object
        self.assertEqual(retrieved_user, user)

    def test_reload(self):
        """
        Test the 'reload' method
        """
        # Create a new object
        user = User()
        self.storage.new(user)

        # Save the storage to the file
        self.storage.save()

        # Reload the storage from the file
        self.storage.reload()

        # Check if the object exists in the storage
        self.assertIn(user, self.storage.all().values())

    def test_count(self):
        """
        Test the 'count' method
        """

        # Create a new object
        user = User()
        self.storage.new(user)

        # Check if the count is correct
        count = self.storage.count()
        all_obj = self.storage.all()
        self.assertEqual(count, len(all_obj))

    def test_count_with_class(self):
        """
        Test the 'count' method
        """

        # Create a new object
        user = User()
        self.storage.new(user)

        # Check if the count is correct
        count = self.storage.count(User)
        all_obj = self.storage.all(User)
        self.assertEqual(count, len(all_obj))

    def test_count_with_class_and_id(self):
        """
        Test the 'count' method
        """

        # Create a new object
        user = User()
        self.storage.new(user)

        # Check if the count is correct
        count = 0
        for obj in self.storage.all(User).values():
            if obj.id == user.id:
                count += 1
            return count
        self.assertEqual(count, self.storage.count(User))


if __name__ == '__main__':
    unittest.main()
