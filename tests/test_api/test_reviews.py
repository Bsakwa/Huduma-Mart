#!/usr/bin/python3

"""
Unittests for Review API endpoints.
"""

import json
import unittest
from flask import Flask
from api.v1.views import app_views
from models import storage
from dotenv import dotenv_values
from models.reviews import Review
from models.engine.db_storage import DBStorage
import os


dotenv_values(".apienv")


class ReviewsAPITestCase(unittest.TestCase):
    def setUp(self):
        # Set up the Flask app
        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.app.config['TESTING'] = True
        self.app.config['ENV'] = 'test'

    def tearDown(self):
        # Reset the storage
        storage.reload()

    def test_get_reviews(self):
        """Test GET /reviews"""
        with self.app.test_client() as client:
            response = client.get('api/v1/reviews')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_get_review(self):
        """Test GET /reviews/<review_id>"""
        with self.app.test_client() as client:
            review = Review()
            storage.new(review)
            storage.save()
            review_id = review.id
            response = client.get('api/v1/reviews/{}'.format(review_id))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_delete_review(self):
        """Test DELETE /reviews/<review_id>"""
        with self.app.test_client() as client:
            review = Review()
            storage.new(review)
            storage.save()
            review_id = review.id
            response = client.delete('api/v1/reviews/{}'.format(review_id))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_update_review(self):
        """Test PUT /reviews/<review_id>"""
        with self.app.test_client() as client:
            # Create a review and save it to the storage
            review = Review()
            storage.new(review)
            storage.save()
            review_id = review.id

            # Update the review with new data
            json_data = {
                'rating': 5,
                'content': 'Excellent service!'
            }

            response = client.put(f'api/v1/reviews/{review_id}',
                                  json=json_data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_delete_review(self):
        """Test DELETE /reviews/<review_id>"""
        with self.app.test_client() as client:
            # Create a review and save it to the storage
            review = Review()
            storage.new(review)
            storage.save()
            review_id = review.id

            response = client.delete(f'api/v1/reviews/{review_id}')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_get_review(self):
        """Test GET /reviews/<review_id>"""
        with self.app.test_client() as client:
            # Create a review and save it to the storage
            review = Review()
            storage.new(review)
            storage.save()

            # Set a non-existing review_id
            review_id = '123456'

            response = client.get(f'api/v1/reviews/{review_id}')
            self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
