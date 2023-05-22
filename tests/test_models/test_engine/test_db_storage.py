#!/usr/bin/python3

"""
Unittest for DBStorage class.
"""

import os
import sqlalchemy
import unittest
from dotenv import load_dotenv
from models.engine import db_storage
from models.location import Location
from models.base_model import BaseModel, Base
from sqlalchemy.orm import Session
DBStorage = db_storage.DBStorage

load_dotenv()


class DBStorageTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case.
        This method will be called before each test function.
        """
        # Create a new instance of DBStorage for testing
        self.storage = DBStorage()
        self.storage.__init__()
        # Reload the database session
        self.storage.reload()

    def tearDown(self):
        """
        Clean up the test case.
        This method will be called after each test function.
        """
        # Close the database session
        self.storage.close()

    def test_database_object_exists(self):
        """
        Test if the database object exists.
        """
        # Check if the database object is not None
        self.assertIsNotNone(self.storage._DBStorage__engine)

    def test_database_session_exists(self):
        """
        Test if the database session exists.
        """
        # Check if the database session is not None
        self.assertIsNotNone(self.storage._DBStorage__session)

    def test_database_session_is_of_type_scoped_session(self):
        """
        Test if the database session is of type scoped_session.
        """
        # Check if the database session is of type scoped_session
        self.assertIsInstance(self.storage._DBStorage__session,
                              sqlalchemy.orm.scoped_session)


if __name__ == '__main__':
    unittest.main()
