#!/usr/bin/python3

"""
This module generates fake categories for testing purposes.
"""

from dotenv import load_dotenv
from faker import Faker
from models.categories import Category
from models import storage
from models.engine.db_storage import DBStorage

fake = Faker()

# Initialize the database
storage = DBStorage()
storage.reload()

# Define the category names and descriptions
category_data = [
    ("Food Vendors", "Delicious street food served with a smile"),
    ("Street Vendors", "Find unique goods from local street vendors"),
    ("Artisans", "Handcrafted creations that showcase true artistry"),
    ("House Cleaners", "Professional cleaning services for your home"),
    ("Laundry Services", "Convenient laundry solutions for busy individuals"),
    ("Car Washers", "Give your vehicle a sparkling clean wash"),
    ("Gardeners", "Transform your outdoor space with expert gardening"),
    ("Tailors and Seamstresses", "Custom-made clothing tailored to perfection"),
    ("Shoe Repairers", "Restore and repair your favorite shoes"),
    ("Handicrafts", "One-of-a-kind handmade crafts with intricate designs"),
    ("Plumbers", "Skilled plumbers for all your plumbing needs"),
    ("Electricians", "Professional electricians ensuring safety and quality"),
    ("House Painters", "Enhance your space with professional painting services"),
    ("Hairdressers and Barbers", "Experience stylish haircuts and grooming"),
    ("Mechanics", "Trustworthy mechanics for your vehicle repairs"),
    ("Babysitters", "Reliable care for your little ones"),
    ("Pet Caretakers", "Caring and responsible pet sitting and walking services"),
    ("Event Organizers", "Plan and execute memorable events"),
    ("Tour Guides", "Discover the hidden gems with knowledgeable tour guides"),
    ("Street Performers", "Captivating performances by talented street artists")
]

# Generate random categories and test file
categories = []
with open('fakecategories.txt', 'w') as f:
    for category_name, category_description in category_data:
        category = Category(
            name=category_name,
            description=category_description,
            id=fake.uuid4(),
            created_at=fake.date_time_this_year(),
            updated_at=fake.date_time_this_year()
        )
        categories.append(category)
        category_data = [
            category.name,
            category.description,
            category.id,
            category.created_at,
            category.updated_at
        ]
        f.write(" ".join(str(data) for data in category_data) + "\n")

# Save the categories to the database
for category in categories:
    storage.new(category)
storage.save()
