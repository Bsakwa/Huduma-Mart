#!/usr/bin/python3

"""
This script generates fake users and stores them in a database.
"""

from dotenv import load_dotenv
from faker import Faker
from models.user import User
from models import storage
from models.engine.db_storage import DBStorage

fake = Faker()

# Initialize the database
storage = DBStorage()
storage.reload()

# Generate random users and test file
users = []
with open('fakeusers.txt', 'w') as f:
    for _ in range(5):
        user = User(
            email=fake.email(),
            password=fake.password(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            id=fake.uuid4(),
            created_at=fake.date_time_this_year(),
            updated_at=fake.date_time_this_year()
        )
        users.append(user)
        user_data = [
            user.first_name,
            user.last_name,
            user.email,
            user.password,
            user.id,
            user.created_at,
            user.updated_at
        ]
        f.write(" ".join(str(data) for data in user_data) + "\n")

# Save users to the database
for user in users:
    storage.new(user)
storage.save()
