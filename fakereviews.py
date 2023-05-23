#!/usr/bin/python3

"""
Generates fake reviews for testing purposes
"""

import random
from faker import Faker
from models.reviews import Review
from models.user import User
from models.service_provider import ServiceProvider
from models import storage
from models.engine.db_storage import DBStorage
from datetime import datetime


fake = Faker()

# Get all service providers and users

users = list(storage.all(User).values())
service_providers = list(storage.all(ServiceProvider).values())

# Check if service providers and users exist
if not storage.all(User) or not storage.all(ServiceProvider):
    raise Exception("No users or service providers exist")

# Define the list of reviews with different ratings
review_data = [
    {
        'content': "Great service, highly recommended!",
        'rating': 5
    },
    {
        'content': "Terrible experience, avoid at all costs!",
        'rating': 1
    },
    {
        'content': "Average service, nothing outstanding.",
        'rating': 3
    },
    {
        'content': "Excellent work, very satisfied!",
        'rating': 4
    },
    {
        'content': "Poor service quality, disappointed.",
        'rating': 2
    },
]

# Generate fake reviews
reviews = []

# Define the number of reviews to generate
num_reviews = 2

with open('fakereviews.txt', 'w') as f:
    for i in range(num_reviews):
        user = random.choice(users)
        service_provider = random.choice(service_providers)
        review = random.choice(review_data)

        content = review['content']
        rating = review['rating']
        id = fake.uuid4()
        created_at = datetime.now()
        updated_at = datetime.now()

        review = Review(content=content,
                        rating=rating,
                        user_id=user.id,
                        service_provider_id=service_provider.id,
                        id=fake.uuid4(),
                        created_at=created_at,
                        updated_at=updated_at
                        )
        reviews.append(review)

        # Write to file
        f.write(str(review) + '\n')

# Save reviews to database
for review in reviews:
    storage.new(review)
storage.save()
