#!/usr/bin/env python

"""
This module contains tests for the Location class
"""
import unittest
from models.location import Location

class TestLocation(unittest.TestCase):
    def setUp(self):
        
        # Create an instance of the Location class
        self.location = Location(name='Test Location',
                                 county='Test County',
                                 town='Test Town',
                                 estate='Test Estate')
        pass

    def tearDown(self):
        # Clean up after each test if needed
        pass

    def test_location_creation(self):
        # Test the creation of a Location instance
        location = Location(name='Test Location',
                            county='Test County',
                            town='Test Town',
                            estate='Test Estate')

        self.assertEqual(location.name, 'Test Location')
        self.assertEqual(location.county, 'Test County')
        self.assertEqual(location.town, 'Test Town')
        self.assertEqual(location.estate, 'Test Estate')

    def test_location_properties(self):
        # Test the properties of a Location instance
        location = Location(name='Test Location',
                            county='Test County',
                            town='Test Town',
                            estate='Test Estate')

        self.assertEqual(location.name, 'Test Location')
        self.assertEqual(location.county, 'Test County')
        self.assertEqual(location.town, 'Test Town')
        self.assertEqual(location.estate, 'Test Estate')

    def test_location_methods(self):
        # Test any additional methods or behaviors of the Location class
        location = Location(name='Test Location',
                            county='Test County',
                            town='Test Town', 
                            estate='Test Estate')

    def test_init(self):
        location = Location(name="Nairobi",
                            county="Kiambu",
                            town="Karen",
                            estate="Spring Valley")
        self.assertEqual(location.name, "Nairobi")
        self.assertEqual(location.county, "Kiambu")
        self.assertEqual(location.town, "Karen")
        self.assertEqual(location.estate, "Spring Valley")

    def test_delete(self):
        location = Location(name="Nairobi",
                            county="Kiambu",
                            town="Karen",
                            estate="Spring Valley")
        location.save()
        location.delete()
        self.assertEqual(len(Location.objects()), 0)

    def test_get(self):
        location = Location(name="Nairobi",
                            county="Kiambu",
                            town="Karen",
                            estate="Spring Valley")
        location.save()
        self.assertEqual(Location.get(location.id), location)

        
if __name__ == '__main__':
    unittest.main()

