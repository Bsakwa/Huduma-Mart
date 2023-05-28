#!/usr/bin/python3

"""
Unittests for Category API endpoints.
"""

import json
import unittest
from flask import Flask
from api.v1.views import app_views
from models import storage
from dotenv import dotenv_values
from models.categories import Category
from models.engine.db_storage import DBStorage
import os


dotenv_values(".apienv")


class CategoriesAPITestCase(unittest.TestCase):
    def setUp(self):
        # Set up the Flask app
        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.app.config['TESTING'] = True
        self.app.config['ENV'] = 'test'

    def tearDown(self):
        # Reset the storage
        storage.reload()

    def test_get_all_categories(self):
        """Test GET /categories"""
        with self.app.test_client() as client:
            response = client.get('/api/v1/categories')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_create_category(self):
        """Test POST /categories"""
        with self.app.test_client() as client:
            # Create a new category
            json_data = {
                'name': 'Test Category',
                'description': 'Test Description'
            }

            response = client.post('/api/v1/categories',
                                   json=json_data)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.content_type, 'application/json')

    def test_get_category(self):
        """Test GET /categories/<category_id>"""
        with self.app.test_client() as client:
            category = Category()
            storage.new(category)
            storage.save()
            category_id = category.id

            response = client.get('/api/v1/categories/{}'.format(category_id))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_delete_category(self):
        """Test DELETE /categories/<category_id>"""
        with self.app.test_client() as client:
            category = Category()
            storage.new(category)
            storage.save()
            category_id = category.id

            response = client.delete('/api/v1/categories/{}'
                                     .format(category_id))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_put_category(self):
        """Test PUT /categories/<category_id>"""
        with self.app.test_client() as client:
            # Create a category and save it to the storage
            category = Category()
            storage.new(category)
            storage.save()
            category_id = category.id

            # Update the category with new data
            json_data = {
                'name': 'Updated Category',
                'description': 'Updated Description'
            }

            response = client.put('/api/v1/categories/{}'.format(category_id),
                                  json=json_data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()
