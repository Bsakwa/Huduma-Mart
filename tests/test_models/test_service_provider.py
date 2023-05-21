#!/usr/bin/env python3

"""
This module contains unit tests for the ServiceProvider class.
"""


import unittest
from models.service_provider import ServiceProvider
from models.reviews import Review


class TestServiceProvider(unittest.TestCase):
    def setUp(self):
        # Perform setup tasks, if any
        pass

    def tearDown(self):
        # Perform cleanup tasks, if any
        pass

    def test_create_service_provider(self):
        # Test creating a service provider instance
        # and assert that the attributes are set correctly
        service_provider = ServiceProvider(
            name="John Doe",
            email="johndoe@example.com",
            phone_number="1234567890",
            password="password123",
            description="Lorem ipsum",
            category_id="category_id",
            location_id="location_id"
        )
        self.assertEqual(service_provider.name, "John Doe")
        self.assertEqual(service_provider.email, "johndoe@example.com")
        self.assertEqual(service_provider.phone_number, "1234567890")
        self.assertEqual(service_provider.password, "password123")
        self.assertEqual(service_provider.description, "Lorem ipsum")
        self.assertEqual(service_provider.category_id, "category_id")
        self.assertEqual(service_provider.location_id, "location_id")

    def test_get_description(self):
        # Test getting the description of a service provider
        service_provider = ServiceProvider(description="Lorem ipsum")
        self.assertEqual(service_provider.description, "Lorem ipsum")

    def test_set_description(self):
        # Test setting the description of a service provider
        service_provider = ServiceProvider(description="Lorem ipsum")
        service_provider.description = "Lorem ipsum dolor sit amet"
        self.assertEqual(service_provider.description,
                         "Lorem ipsum dolor sit amet")

    def test_get_category_id(self):
        # Test getting the category ID of a service provider
        service_provider = ServiceProvider(category_id="category_id")
        self.assertEqual(service_provider.category_id, "category_id")

    def test_set_category_id(self):
        # Test setting the category ID of a service provider
        service_provider = ServiceProvider(category_id="category_id")
        service_provider.category_id = "new_category_id"
        self.assertEqual(service_provider.category_id, "new_category_id")

    def test_get_location_id(self):
        # Test getting the location ID of a service provider
        service_provider = ServiceProvider(location_id="location_id")
        self.assertEqual(service_provider.location_id, "location_id")

    def test_set_location_id(self):
        # Test setting the location ID of a service provider
        service_provider = ServiceProvider(location_id="location_id")
        service_provider.location_id = "new_location_id"
        self.assertEqual(service_provider.location_id, "new_location_id")

    def test_get_name(self):
        # Test getting the name of a service provider
        service_provider = ServiceProvider(name="John Doe")
        self.assertEqual(service_provider.name, "John Doe")

    def test_set_name(self):
        # Test setting the name of a service provider
        service_provider = ServiceProvider(name="John Doe")
        service_provider.name = "Jane Doe"
        self.assertEqual(service_provider.name, "Jane Doe")

    def test_get_email(self):
        # Test getting the email of a service provider
        service_provider = ServiceProvider(email="b@gmail.com")
        self.assertEqual(service_provider.email, "b@gmail.com")

    def test_set_email(self):
        # Test setting the email of a service provider
        service_provider = ServiceProvider(email="b@gmail.com")
        service_provider.email = "c@gmail.com"
        self.assertEqual(service_provider.email, "c@gmail.com")

    def test_get_phone_number(self):
        # Test getting the phone number of a service provider
        service_provider = ServiceProvider(phone_number="1234567890")
        self.assertEqual(service_provider.phone_number, "1234567890")

    def test_set_phone_number(self):
        # Test setting the phone number of a service provider
        service_provider = ServiceProvider(phone_number="1234567890")
        service_provider.phone_number = "0987654321"
        self.assertEqual(service_provider.phone_number, "0987654321")

    def test_get_password(self):
        # Test getting the password of a service provider
        service_provider = ServiceProvider(password="password123")
        self.assertEqual(service_provider.password, "password123")

    def test_set_password(self):
        # Test setting the password of a service provider
        service_provider = ServiceProvider(password="password123")
        service_provider.password = "password456"
        self.assertEqual(service_provider.password, "password456")

    def test_get_id(self):
        # Test getting the ID of a service provider
        service_provider = ServiceProvider(id="id")
        self.assertEqual(service_provider.id, "id")

    def test_set_id(self):
        # Test setting the ID of a service provider
        service_provider = ServiceProvider(id="id")
        service_provider.id = "new_id"
        self.assertEqual(service_provider.id, "new_id")

    def test_set_reviews(self):
        # Test setting the reviews of a service provider
        service_provider = ServiceProvider(reviews=[Review()])
        service_provider.reviews = [Review(), Review()]
        self.assertEqual(len(service_provider.reviews), 2)
        self.assertIsInstance(service_provider.reviews[0], Review)
        self.assertIsInstance(service_provider.reviews[1], Review)

    def test_get_rating(self):
        # Test getting the rating of a service provider
        service_provider = ServiceProvider(rating=4.5)
        self.assertEqual(service_provider.rating, 4.5)

    def test_set_rating(self):
        # Test setting the rating of a service provider
        service_provider = ServiceProvider(rating=4.5)
        service_provider.rating = 3.5
        self.assertEqual(service_provider.rating, 3.5)

    def test_get_rating_count(self):
        # Test getting the rating count of a service provider
        service_provider = ServiceProvider(rating_count=10)
        self.assertEqual(service_provider.rating_count, 10)

    def test_add_multiple_reviews(self):
        """Test adding multiple reviews to a service provider"""
        service_provider = ServiceProvider(name="John Doe")
        review1 = Review(rating=4, comment="Great service")
        review2 = Review(rating=5, comment="Excellent work")
        service_provider.reviews = [review1, review2]
        self.assertEqual(len(service_provider.reviews), 2)
        self.assertIn(review1, service_provider.reviews)
        self.assertIn(review2, service_provider.reviews)

if __name__ == "__main__":
    unittest.main()
