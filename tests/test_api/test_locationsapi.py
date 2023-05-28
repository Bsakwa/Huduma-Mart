#!/usr/bin/python3

"""
Unittests for Location API endpoints.
"""

import json
import unittest
from flask import Flask
from api.v1.views import app_views
from models import storage
from dotenv import dotenv_values
from models.location import Location
from models.service_provider import ServiceProvider
from models.engine.db_storage import DBStorage
import os


dotenv_values(".apienv")


class LocationsAPITestCase(unittest.TestCase):
    def setUp(self):
        # Set up the Flask app
        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.app.config['TESTING'] = True
        self.app.config['ENV'] = 'test'

    def tearDown(self):
        # Reset the storage
        storage.reload()

    def test_get_all_locations(self):
        """Test GET /locations"""
        with self.app.test_client() as client:
            response = client.get('/api/v1/locations')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_create_location(self):
        """Test POST /locations"""
        with self.app.test_client() as client:
            # Create a new location
            json_data = {
                'name': 'Test Location',
                'county': 'Test County',
                'town': 'Test Town',
                'estate': 'Test Estate'
            }

            response = client.post('/api/v1/locations',
                                   json=json_data)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.content_type, 'application/json')

    def test_get_location(self):
        """Test GET /locations/<location_id>"""
        with self.app.test_client() as client:
            location = Location()
            storage.new(location)
            storage.save()
            location_id = location.id

            response = client.get('/api/v1/locations/{}'.format(location_id))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_put_location(self):
        """Test PUT /locations/<location_id>"""
        with self.app.test_client() as client:
            # Create a location and save it to the storage
            location = Location()
            storage.new(location)
            storage.save()
            location_id = location.id

            # Update the location with new data
            json_data = {
                'name': 'Updated Location',
                'county': 'Updated County',
                'town': 'Updated Town',
                'estate': 'Updated Estate'
            }

            response = client.put('/api/v1/locations/{}'.format(location_id),
                                  json=json_data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_delete_location(self):
        """
        Test DELETE /locations/<location_id>
        """
        with self.app.test_client() as client:
            location = Location()
            storage.new(location)
            storage.save()
            location_id = location.id

            response = client.delete('/api/v1/locations/{}'
                                     .format(location_id))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()
