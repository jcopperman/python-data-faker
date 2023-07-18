import json
from faker import Faker
import random

# Initialize Faker
fake = Faker(["en_US"])  # Set the locale to United States (English)

def generate_sa_id_number():
    # Generate valid South African ID number
    birth_date = fake.date_of_birth().strftime("%y%m%d")  # Get birth date in YYMMDD format
    gender_digits = str(random.randint(0, 9999)).zfill(4)  # Generate 4 random digits for gender
    citizen_checksum = str(random.randint(0, 999)).zfill(3)  # Generate 3 digits for citizen and checksum digit

    id_number = birth_date + gender_digits + citizen_checksum

    return id_number

data = []

# Loop through range up to 100
for val in range(100):
    item = {
        "ID": generate_sa_id_number(),  # Generate a unique and valid South African ID number
        "Name": fake.name(),
        "Lastname": fake.last_name(),
        "PhoneNumber": fake.phone_number(),
        "Country": fake.country(),
        "Text": fake.text(),
        "Date": fake.date()
    }
    data.append(item)

# Write data to JSON file
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data written to output.json file.")
