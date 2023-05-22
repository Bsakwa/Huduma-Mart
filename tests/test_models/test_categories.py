#!/usr/bin/env python3

"""
Test cases for the Category class
"""

from models.engine.file_storage import FileStorage
import models
import unittest
from models.categories import Category
from models.service_provider import ServiceProvider
from models import storage


class CategoryTests(unittest.TestCase):
    """
    Test cases for the Category class
    """
    def test_init(self):
        """
        Test that the constructor of the Category class
        has the correct output
        """
        name = "Electrician"
        category = Category(name=name)

        self.assertEqual(category.name, name)
        self.assertEqual(category.service_providers, [])

    def test_str(self):
        """
        Test that the str method has the correct output
        """
        category = Category(name="Electrician")
        expected_string = "[Category] ({}) {}".format(category.id,
                                                      category.__dict__)
        self.assertEqual(expected_string, str(category))

    def test_repr(self):
        """
        Test that the repr method has the correct output
        """
        category = Category(name="Electrician")
        expected_string = f"[Category] ({category.id}) {category.__dict__}"
        self.assertEqual(expected_string, repr(category))

    def test_add_service_provider(self):
        """
        Test adding a service provider to the category
        """
        category = Category(name="Electrician")
        service_provider = ServiceProvider(name="John Doe")
        category.add_service_provider(service_provider)
        self.assertIn(service_provider, category.service_providers)

    def test_remove_service_provider(self):
        """
        Test removing a service provider from the category
        """
        category = Category(name="Electrician")
        service_provider = ServiceProvider(name="John Doe")
        category.service_providers.append(service_provider)
        category.service_providers.remove(service_provider)
        self.assertNotIn(service_provider, category.service_providers)

    def test_to_dict(self):
        """
        Test that the to_dict method has the correct output
        """
        category = Category(name="Electrician")
        expected = {
                "name": "Electrician",
                "service_providers": []
                }

        category_dict = category.to_dict()
        for key in expected.keys():
            self.assertEqual(expected[key], category_dict[key])

    def test_delete(self):
        """
        Test that the delete method has the correct output
        """
        category = Category(name="Electrician")
        category.save()
        category.delete()
        self.assertNotIn(category, storage.all().values())

    def test_update_name(self):
        """
        Test if the update method has the correct output
        """
        category = Category(name="Electrician")
        new_name = "Plumber"
        category.name = new_name
        self.assertEqual(category.name, new_name)

    def test_add_multiple_service_providers(self):
        """
        Test adding multiple service providers to the category
        """
        category = Category(name="Electrician")
        service_provider1 = ServiceProvider(name="John Doe")
        service_provider2 = ServiceProvider(name="Jane Smith")
        category.add_service_provider(service_provider1)
        category.add_service_provider(service_provider2)
        self.assertIn(service_provider1, category.service_providers)
        self.assertIn(service_provider2, category.service_providers)


if __name__ == "__main__":
    unittest.main()
