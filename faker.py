import json
from faker import Faker
import random

# Initialize Faker
fake = Faker(["en_US"])  # Set the locale to United States (English)

def generate_sa_id_number():
    # Generate valid South African ID number
    birth_date = fake.date_of_birth().strftime("%y%m%d")  # Get birth date in YYMMDD format
    random_digits = str(random.randint(0, 9999)).zfill(4)  # Generate 4 random digits
    race_and_sex = str(random.randint(0, 999)).zfill(3)  # Generate 3 digits for race and sex

    id_number = birth_date + random_digits + race_and_sex

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
