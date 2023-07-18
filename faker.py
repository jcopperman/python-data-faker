import json
from faker import Faker
import random

# Initialize Faker
fake = Faker()

def generate_sa_id_number():
    # Generate valid South African ID number
    birth_date = fake.date_of_birth().strftime("%y%m%d")  # Get birth date in YYMMDD format
    random_gender_digits = str(random.randint(0, 9999)).zfill(4)  # Generate 4 random digits
    citizen_and_checksum = str(random.randint(0, 999)).zfill(3)  # Generate 3 digits for race and sex

    id_number = birth_date + random_gender_digits + citizen_and_checksum

    return id_number

def generate_phone_number():
    # Generate phone number with 9 digits and no special characters
    phone_number = fake.numerify(text="#########")  # Replace '#' with random digits
    return phone_number

def generate_test_card_number(provider):
    # Generate test card number for Visa or Mastercard
    if provider == "visa":
        card_number = fake.credit_card_number(card_type="visa")
    elif provider == "mastercard":
        card_number = fake.credit_card_number(card_type="mastercard")
    else:
        card_number = None

    return card_number

def generate_account_balance():
    # Generate account balance between 0 and 10,000
    account_balance = round(random.uniform(0, 10000), 2)
    return account_balance

data = []

# Loop through range up to 100
for val in range(100):
    item = {
        "ID": generate_sa_id_number(),  # Generate a unique and valid South African ID number
        "Name": fake.name(),
        "Lastname": fake.last_name(),
        "PhoneNumber": generate_phone_number(),  # Generate a phone number with 9 digits and no special characters
        "Country": fake.country(),
        "Text": fake.text(),
        "Date": fake.date(),
        "VisaCardNumber": generate_test_card_number("visa"),  # Generate a Visa test card number
        "MastercardNumber": generate_test_card_number("mastercard"),  # Generate a Mastercard test card number
        "AccountBalance": generate_account_balance(),  # Generate an account balance
    }
    data.append(item)

# Write data to JSON file
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data written to output.json file.")
