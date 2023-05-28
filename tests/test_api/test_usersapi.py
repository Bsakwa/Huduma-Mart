#!/usr/bin/python3

"""
Test suite for the users API endpoints
"""

import json
import unittest
from flask import Flask
from api.v1.views import app_views
from models import storage
from models.user import User
from models.reviews import Review
from models.service_provider import ServiceProvider
from dotenv import dotenv_values

dotenv_values(".apienv")


class UsersAPITestCase(unittest.TestCase):
    def setUp(self):
        # Set up the Flask app
        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.app.config['TESTING'] = True
        self.app.config['ENV'] = 'test'

    def tearDown(self):
        # Reset the storage
        storage.reload()

    def test_get_users(self):
        """Test GET /users"""
        with self.app.test_client() as client:
            response = client.get('api/v1/users')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_get_user(self):
        """Test GET /users/<user_id>"""
        with self.app.test_client() as client:
            user = User(email='test@example.com', password='password')
            storage.new(user)
            storage.save()
            user_id = user.id
            response = client.get(f'api/v1/users/{user_id}')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_post_user(self):
        """Test POST /users"""
        with self.app.test_client() as client:
            json_data = {
                'email': 'test@example.com',
                'password': 'password'
            }
            response = client.post('api/v1/users', json=json_data)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.content_type, 'application/json')

    def test_put_user(self):
        """Test PUT /users/<user_id>"""
        with self.app.test_client() as client:
            user = User(email='test@example.com', password='password')
            storage.new(user)
            storage.save()
            user_id = user.id

            json_data = {
                'email': 'updated@example.com',
                'password': 'updated_password'
            }
            response = client.put(f'api/v1/users/{user_id}', json=json_data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_delete_user(self):
        """Test DELETE /users/<user_id>"""
        with self.app.test_client() as client:
            user = User(email='test@example.com', password='password')
            storage.new(user)
            storage.save()
            user_id = user.id
            response = client.delete(f'api/v1/users/{user_id}')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()
