#!/usr/bin/python3

"""
This script generates fake locations for testing purposes.
"""

from faker import Faker
from models.location import Location
from models import storage
from models.engine.db_storage import DBStorage
import random

fake = Faker()

# Define the counties, towns, and estates
counties = [
    ("Mombasa", 1),
    ("Kwale", 2),
    ("Kilifi", 3),
    ("Tana River", 4),
    ("Lamu", 5),
    ("Taita-Taveta", 6),
    ("Garissa", 7),
    ("Wajir", 8),
    ("Mandera", 9),
    ("Marsabit", 10),
    ("Isiolo", 11),
    ("Meru", 12),
    ("Tharaka-Nithi", 13),
    ("Embu", 14),
    ("Kitui", 15),
    ("Machakos", 16),
    ("Makueni", 17),
    ("Nyandarua", 18),
    ("Nyeri", 19),
    ("Kirinyaga", 20),
    ("Murang'a", 21),
    ("Kiambu", 22),
    ("Turkana", 23),
    ("West Pokot", 24),
    ("Samburu", 25),
    ("Trans Nzoia", 26),
    ("Uasin Gishu", 27),
    ("Elgeyo-Marakwet", 28),
    ("Nandi", 29),
    ("Baringo", 30),
    ("Laikipia", 31),
    ("Nakuru", 32),
    ("Narok", 33),
    ("Kajiado", 34),
    ("Kericho", 35),
    ("Bomet", 36),
    ("Kakamega", 37),
    ("Vihiga", 38),
    ("Bungoma", 39),
    ("Busia", 40),
    ("Siaya", 41),
    ("Kisumu", 42),
    ("Homa Bay", 43),
    ("Migori", 44),
    ("Kisii", 45),
    ("Nyamira", 46),
    ("Nairobi", 47)
]

towns_estates = {
    "Mombasa": ["Mombasa", "Nyali", "Mtwapa"],
    "Kwale": ["Kwale", "Diani"],
    "Kilifi": ["Kilifi", "Malindi"],
    "Tana River": ["Hola", "Garsen"],
    "Lamu": ["Lamu Town", "Shela"],
    "Taita-Taveta": ["Voi", "Wundanyi"],
    "Garissa": ["Garissa", "Modogashe"],
    "Wajir": ["Wajir", "Mandera"],
    "Mandera": ["Mandera", "Takaba"],
    "Marsabit": ["Marsabit", "Laisamis"],
    "Isiolo": ["Isiolo", "Moyale"],
    "Meru": ["Meru", "Embu"],
    "Tharaka-Nithi": ["Kathwana", "Chuka"],
    "Embu": ["Embu", "Siakago"],
    "Kitui": ["Kitui", "Mwingi"],
    "Machakos": ["Machakos", "Athi River"],
    "Makueni": ["Wote", "Makindu"],
    "Nyandarua": ["Ol Kalou", "Ndaragwa"],
    "Nyeri": ["Nyeri", "Karatina"],
    "Kirinyaga": ["Kerugoya", "Sagana"],
    "Murang'a": ["Murang'a", "Kenol"],
    "Kiambu": ["Kiambu", "Thika"],
    "Turkana": ["Lodwar", "Kakuma"],
    "West Pokot": ["Kapenguria", "Lodokejek"],
    "Samburu": ["Maralal", "Baragoi"],
    "Trans Nzoia": ["Kitale", "Kiminini"],
    "Uasin Gishu": ["Eldoret", "Burnt Forest"],
    "Elgeyo-Marakwet": ["Iten", "Kapsowar"],
    "Nandi": ["Kapsabet", "Eldoret"],
    "Baringo": ["Kabarnet", "Eldama Ravine"],
    "Laikipia": ["Nanyuki", "Rumuruti"],
    "Nakuru": ["Nakuru", "Naivasha"],
    "Narok": ["Narok", "Mai Mahiu"],
    "Kajiado": ["Kajiado", "Ngong"],
    "Kericho": ["Kericho", "Bureti"],
    "Bomet": ["Bomet", "Longisa"],
    "Kakamega": ["Kakamega", "Webuye"],
    "Vihiga": ["Vihiga", "Chavakali"],
    "Bungoma": ["Bungoma", "Kimilili"],
    "Busia": ["Busia", "Malaba"],
    "Siaya": ["Siaya", "Ugunja"],
    "Kisumu": ["Kisumu City", "Muhoroni"],
    "Homa Bay": ["Homa Bay", "Oyugis"],
    "Migori": ["Migori", "Awendo"],
    "Kisii": ["Kisii", "Ogembo"],
    "Nyamira": ["Nyamira", "Keroka"],
    "Nairobi": ["Nairobi CBD", "Westlands"]
}

# Initialize the database
storage = DBStorage()
storage.reload()

# Generate random locations and test file
locations = []
with open('fakelocations.txt', 'w') as f:
    for county_name, county_number in counties:
        town_estates = towns_estates[county_name]
        town = random.choice(town_estates)
        estates = towns_estates.get(town)

        if estates:
            estate = random.choice(estates)

        estate = random.choice(town_estates)

        location = Location(
            name=county_name,
            county=county_number,
            town=town,
            estate=estate,
            id=fake.uuid4(),
            created_at=fake.date_time_this_year(),
            updated_at=fake.date_time_this_year()
        )
        locations.append(location)
        location_data = [
            location.name,
            location.county,
            location.town,
            location.estate,
            location.id,
            location.created_at,
            location.updated_at
        ]
        f.write(" ".join(str(data) for data in location_data) + "\n")

# save the locations to the database
for location in locations:
    storage.new(location)
storage.save()
