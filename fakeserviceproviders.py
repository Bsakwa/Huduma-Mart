#!/usr/bin/python3

"""
This module defines the FakeServiceProvider class
"""

import random
import models
from faker import Faker
from models.service_provider import ServiceProvider
from models.categories import Category
from models.location import Location
from models import storage
from datetime import datetime

fake = Faker()

# Get all categories and locations from the database
categories = list(storage.all(Category).values())
locations = list(storage.all(Location).values())

# Determine the number of service providers to create
num_providers = 3

if not categories or not locations:
    raise Exception("No categories or locations found in the database.")

service_providers = []

with open("fakeservicepro.txt", "w") as file:
    for i in range(num_providers):
        # Select a random category and location
        category = random.choice(categories)
        location = random.choice(locations)

        # Ensure that the category and location are valid
        while category not in categories or location not in locations:
            category = random.choice(categories)
            location = random.choice(locations)

        name = fake.name()
        description = fake.text(max_nb_chars=10)
        email = fake.email()
        phone_number = fake.phone_number()
        password = fake.password()
        id = fake.uuid4()
        created_at = datetime.now()
        updated_at = datetime.now()

        # Create a new service provider instance
        service_provider = ServiceProvider(
                        name=name,
                        description=description,
                        email=email,
                        phone_number=phone_number,
                        password=password,
                        category=category,
                        location_id=location.id,
                        id=id,
                        created_at=created_at,
                        updated_at=updated_at
                        )

        # Add the service provider to the list
        service_providers.append(service_provider)

        # Write the service provider to the file
        file.write(str(service_provider) + "\n")

# Save the service providers to the database
for service_provider in service_providers:
    storage.new(service_provider)
storage.save()
