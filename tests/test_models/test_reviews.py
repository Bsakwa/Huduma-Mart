#!/usr/bin/env python3

"""This module tests the Review class"""

import unittest
from models.reviews import Review

class ReviewTestCase(unittest.TestCase):
    def setUp(self):
        self.review_data = {
            'content': 'This is a review',
            'rating': 5,
            'user_id': 'user-123',
            'service_provider_id': 'provider-456'
        }

    def tearDown(self):
        self.review_data = None

    def test_review_instance(self):
        review = Review(**self.review_data)
        self.assertEqual(review.content, self.review_data['content'])
        self.assertEqual(review.rating, self.review_data['rating'])
        self.assertEqual(review.user_id, self.review_data['user_id'])
        self.assertEqual(review.service_provider_id, self.review_data['service_provider_id'])

    def test_review_str_representation(self):
        review = Review(**self.review_data)
        expected_str = '[Review] ({}) {}'.format(review.id, review.__dict__)

        self.assertEqual(str(review), expected_str)

    def test_review_init_with_kwargs(self):
        kwargs = {
            'id': 'review-789',
            'content': 'Another review',
            'rating': 4,
            'user_id': 'user-987',
            'service_provider_id': 'provider-654',
            'created_at': '2023-07-15T12:34:56.789012',
            'updated_at': '2023-07-15T12:34:56.789012'
        }
        review = Review(**kwargs)
        self.assertEqual(review.id, kwargs['id'])
        self.assertEqual(review.content, kwargs['content'])
        self.assertEqual(review.rating, kwargs['rating'])
        self.assertEqual(review.user_id, kwargs['user_id'])
        self.assertEqual(review.service_provider_id, kwargs['service_provider_id'])
        self.assertEqual(review.created_at.isoformat(), kwargs['created_at'])
        self.assertEqual(review.updated_at.isoformat(), kwargs['updated_at'])

    def test_review_to_dict(self):
        review = Review(**self.review_data)
        review_dict = review.to_dict()
        self.assertEqual(review_dict['id'], review.id)
        self.assertEqual(review_dict['content'], review.content)
        self.assertEqual(review_dict['rating'], review.rating)
        self.assertEqual(review_dict['user_id'], review.user_id)
        self.assertEqual(review_dict['service_provider_id'], review.service_provider_id)
        self.assertEqual(review_dict['created_at'], review.created_at.isoformat())
        self.assertEqual(review_dict['updated_at'], review.updated_at.isoformat())

    def test_review_to_dict_with_params(self):
        review = Review(**self.review_data)
        review_dict = review.to_dict(['id', 'content'])
        self.assertEqual(review_dict['id'], review.id)
        self.assertEqual(review_dict['content'], review.content)
        self.assertTrue('rating' in review_dict)
        self.assertTrue('user_id' in review_dict)
        self.assertTrue('service_provider_id' in review_dict)
        self.assertTrue('created_at' in review_dict)
        self.assertTrue('updated_at' in review_dict)

    def test_review_to_dict_with_none_params(self):
        review = Review(**self.review_data)
        review_dict = review.to_dict(None)
        self.assertEqual(review_dict['id'], review.id)
        self.assertEqual(review_dict['content'], review.content)
        self.assertEqual(review_dict['rating'], review.rating)
        self.assertEqual(review_dict['user_id'], review.user_id)
        self.assertEqual(review_dict['service_provider_id'], review.service_provider_id)
        self.assertEqual(review_dict['created_at'], review.created_at.isoformat())
        self.assertEqual(review_dict['updated_at'], review.updated_at.isoformat())

    def test_review_to_dict_with_empty_list_params(self):
        review = Review(**self.review_data)
        review_dict = review.to_dict([])
        self.assertEqual(review_dict['id'], review.id)
        self.assertEqual(review_dict['content'], review.content)
        self.assertEqual(review_dict['rating'], review.rating)
        self.assertEqual(review_dict['user_id'], review.user_id)
        self.assertEqual(review_dict['service_provider_id'], review.service_provider_id)
        self.assertEqual(review_dict['created_at'], review.created_at.isoformat())
        self.assertEqual(review_dict['updated_at'], review.updated_at.isoformat())

    def test_review_to_dict_with_wrong_params(self):
        review = Review(**self.review_data)
        review_dict = review.to_dict(['id', 'content', 'wrong_param'])
        self.assertEqual(review_dict['id'], review.id)
        self.assertEqual(review_dict['content'], review.content)
        self.assertTrue('rating' in review_dict)
        self.assertTrue('user_id' in review_dict)
        self.assertTrue('service_provider_id' in review_dict)
        self.assertTrue('created_at' in review_dict)
        self.assertTrue('updated_at' in review_dict)

    def test_review_to_dict_with_empty_string_params(self):
        review = Review(**self.review_data)
        review_dict = review.to_dict(['id', 'content', ''])
        self.assertEqual(review_dict['id'], review.id)
        self.assertEqual(review_dict['content'], review.content)
        self.assertTrue('rating' in review_dict)
        self.assertTrue('user_id' in review_dict)
        self.assertTrue('service_provider_id' in review_dict)
        self.assertTrue('created_at' in review_dict)
        self.assertTrue('updated_at' in review_dict)

    def test_review_to_dict_with_none_string_params(self):
        review = Review(**self.review_data)
        review_dict = review.to_dict(['id', 'content', None])
        self.assertEqual(review_dict['id'], review.id)
        self.assertEqual(review_dict['content'], review.content)
        self.assertTrue('rating' in review_dict)
        self.assertTrue('user_id' in review_dict)
        self.assertTrue('service_provider_id' in review_dict)
        self.assertTrue('created_at' in review_dict)
        self.assertTrue('updated_at' in review_dict)

    def test_review_to_dict_with_int_params(self):
        review = Review(**self.review_data)
        review_dict = review.to_dict([1, 2, 3])
        self.assertEqual(review_dict['id'], review.id)
        self.assertEqual(review_dict['content'], review.content)
        self.assertTrue('rating' in review_dict)
        self.assertTrue('user_id' in review_dict)
        self.assertTrue('service_provider_id' in review_dict)
        self.assertTrue('created_at' in review_dict)
        self.assertTrue('updated_at' in review_dict)

    def test_get_review_by_id(self):
        """Test that a review can be retrieved by ID."""
        review = Review(
                content="This is a review",
                rating=5,
                user_id="1",
                service_provider_id="2",
                )
        review.save()

        retrieved_review = Review.get_by_id(review.id)

        self.assertIsNotNone(retrieved_review)
        self.assertEqual(retrieved_review.id, review.id)
        self.assertEqual(retrieved_review.content, review.content)
        self.assertEqual(retrieved_review.rating, review.rating)
        self.assertEqual(retrieved_review.user_id, review.user_id)
        self.assertEqual(retrieved_review.service_provider_id, review.service_provider_id)

    def test_get_review_by_id_with_invalid_id(self):
        """Test that an invalid ID returns None."""
        review = Review.get_by_id(1)
        self.assertIsNone(review)

    def test_get_review_by_id_with_invalid_type(self):
        """Test that an invalid ID type returns None."""
        review = Review.get_by_id("1")
        self.assertIsNone(review)

    def test_get_review_by_id_with_none(self):
        """Test that None returns None."""
        review = Review.get_by_id(None)
        self.assertIsNone(review)

    def test_get_review_by_id_with_empty_string(self):
        """Test that an empty string returns None."""
        review = Review.get_by_id("")
        self.assertIsNone(review)

    def test_get_review_by_id_with_list(self):
        """Test that a list returns None."""
        review = Review.get_by_id([])
        self.assertIsNone(review)

    def test_get_review_by_id_with_dict(self):
        """Test that a dict returns None."""
        review = Review.get_by_id({})
        self.assertIsNone(review)

    def test_get_review_by_id_with_float(self):
        """Test that a float returns None."""
        review = Review.get_by_id(1.0)
        self.assertIsNone(review)


if __name__ == '__main__':
    unittest.main()
