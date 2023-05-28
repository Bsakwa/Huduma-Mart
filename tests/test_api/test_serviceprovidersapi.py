#!/usr/bin/python3

"""
Unittests for Service Provider API endpoints.
"""

import json
import unittest
from flask import Flask
from api.v1.views import app_views
from models import storage
from dotenv import dotenv_values
from models.service_provider import ServiceProvider
from models.engine.db_storage import DBStorage
import os


dotenv_values(".apienv")


class ServiceProvidersAPITestCase(unittest.TestCase):
    def setUp(self):
        # Set up the Flask app
        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.app.config['TESTING'] = True
        self.app.config['ENV'] = 'test'

    def tearDown(self):
        # Reset the storage
        storage.reload()

    def test_get_all_service_providers(self):
        """Test GET /service_providers"""
        with self.app.test_client() as client:
            response = client.get('/api/v1/service_providers')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

 
if __name__ == '__main__':
    unittest.main()
