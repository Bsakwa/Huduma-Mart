#!/usr/bin/python3

"""
TestUser module
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def test_init(self):
        user = User(email="john@example.com",
                    password="password",
                    first_name="John",
                    last_name="Doe")
        self.assertEqual(user.email, "john@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_str(self):
        user = User(email="john@example.com",
                    password="password",
                    first_name="John",
                    last_name="Doe")
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_to_dict(self):
        """test to_dict method creates a dict"""
        u = User()
        d = u.to_dict()
        self.assertEqual(type(d), dict)

    def test_save(self):
        """test save method updates `updated_at`"""
        u = User()
        u.save()
        self.assertNotEqual(u.created_at, u.updated_at)

    def test_save_to_file(self):
        """test that save_to_file creates a file"""
        u = User()
        u.save()
        with open("file.json", "r") as f:
            self.assertIn(u.id, f.read())


if __name__ == '__main__':
    unittest.main()
