import json
from faker import Faker
import random

# Initialize Faker
fake = Faker()
Faker.seed(1234)  # Set the seed for Faker

# List of South African provinces
sa_provinces = [
    "Eastern Cape",
    "Free State",
    "Gauteng",
    "KwaZulu-Natal",
    "Limpopo",
    "Mpumalanga",
    "North West",
    "Northern Cape",
    "Western Cape"
]

# List of Namibian regions
na_regions = [
    "Erongo",
    "Hardap",
    "Karas",
    "Kavango East",
    "Kavango West",
    "Khomas",
    "Kunene",
    "Ohangwena",
    "Omaheke",
    "Omusati",
    "Oshana",
    "Oshikoto",
    "Otjozondjupa",
    "Zambezi"
]

def generate_sa_id_number(gender):
    # Generate valid South African ID number
    birth_date = fake.date_of_birth().strftime("%y%m%d")  # Get birth date in YYMMDD format
    if gender == "Female":
        random_gender_digits = str(random.randint(0, 4999)).zfill(4)  # Generate 4 random digits for females
    else:
        random_gender_digits = str(random.randint(5000, 9999)).zfill(4)  # Generate 4 random digits for males
    citizenship_and_checksum = str(random.randint(0, 999)).zfill(3)  # Generate 3 digits for race and sex

    id_number = birth_date + random_gender_digits + citizenship_and_checksum

    return id_number

def generate_na_id_number(gender):
    # Generate valid Namibian ID number
    birth_date = fake.date_of_birth().strftime("%y%m%d")  # Get birth date in YYMMDD format
    if gender == "Female":
        random_gender_digit = random.randint(0, 4) * 2 + 1  # Generate 1 random odd digit for females
    else:
        random_gender_digit = random.randint(0, 4) * 2  # Generate 1 random even digit for males
    random_digits = str(random.randint(0, 9999)).zfill(4)  # Generate 4 random digits

    id_number = birth_date + str(random_gender_digit) + random_digits

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

def generate_province():
    # Generate a random province from the list
    province = random.choice(sa_provinces)
    return province

def generate_region():
    # Generate a random region from the list
    region = random.choice(na_regions)
    return region

def generate_postal_code():
    # Generate a random postal code ranging from 0000 to 9999
    postal_code = str(random.randint(0, 9999)).zfill(4)
    return postal_code

data = []

# Loop through range up to 100
for val in range(100):
    gender = fake.random_element(["Female", "Male"])  # Randomly choose a gender
    item = {
        "ID": generate_sa_id_number(gender),  # Generate a unique and valid South African ID number based on gender
        "Name": fake.first_name_female() if gender == "Female" else fake.first_name_male(),
        "Lastname": fake.last_name(),
        "PhoneNumber": generate_phone_number(),  # Generate a phone number with 9 digits and no special characters
        "Country": "South Africa",  # Set the default country as South Africa
        "Text": fake.text(),
        "Date": fake.date(),
        "VisaCardNumber": generate_test_card_number("visa"),  # Generate a Visa test card number
        "MastercardNumber": generate_test_card_number("mastercard"),  # Generate a Mastercard test card number
        "AccountBalance": generate_account_balance(),  # Generate an account balance
        "Province": generate_province(),  # Generate a random province
        "PostalCode": generate_postal_code(),  # Generate a random postal code
        "Gender": gender,  # Add the gender to the item object
    }
    data.append(item)

    # Generate additional data item with Namibian ID number
    na_gender = "Female" if gender == "Female" else "Male"
    na_item = {
        "ID": generate_na_id_number(na_gender),  # Generate a unique and valid Namibian ID number based on gender
        "Name": fake.first_name_female() if na_gender == "Female" else fake.first_name_male(),
        "Lastname": fake.last_name(),
        "PhoneNumber": generate_phone_number(),  # Generate a phone number with 9 digits and no special characters
        "Country": "Namibia",  # Set the default country as Namibia
        "Text": fake.text(),
        "Date": fake.date(),
        "VisaCardNumber": generate_test_card_number("visa"),  # Generate a Visa test card number
        "MastercardNumber": generate_test_card_number("mastercard"),  # Generate a Mastercard test card number
        "AccountBalance": generate_account_balance(),  # Generate an account balance
        "Region": generate_region(),  # Generate a random region in Namibia
        "PostalCode": generate_postal_code(),  # Generate a random postal code
        "Gender": na_gender,  # Add the gender to the item object
    }
    data.append(na_item)

# Write data to JSON file
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data written to output.json file.")
import json
from faker import Faker
import random

# Initialize Faker
fake = Faker()
Faker.seed(1234)  # Set the seed for Faker

# List of South African provinces
sa_provinces = [
    "Eastern Cape",
    "Free State",
    "Gauteng",
    "KwaZulu-Natal",
    "Limpopo",
    "Mpumalanga",
    "North West",
    "Northern Cape",
    "Western Cape"
]

# List of Namibian regions
na_regions = [
    "Erongo",
    "Hardap",
    "Karas",
    "Kavango East",
    "Kavango West",
    "Khomas",
    "Kunene",
    "Ohangwena",
    "Omaheke",
    "Omusati",
    "Oshana",
    "Oshikoto",
    "Otjozondjupa",
    "Zambezi"
]

def generate_sa_id_number(gender):
    # Generate valid South African ID number
    birth_date = fake.date_of_birth().strftime("%y%m%d")  # Get birth date in YYMMDD format
    if gender == "Female":
        random_gender_digits = str(random.randint(0, 4999)).zfill(4)  # Generate 4 random digits for females
    else:
        random_gender_digits = str(random.randint(5000, 9999)).zfill(4)  # Generate 4 random digits for males
    citizenship_and_checksum = str(random.randint(0, 999)).zfill(3)  # Generate 3 digits for race and sex

    id_number = birth_date + random_gender_digits + citizenship_and_checksum

    return id_number

def generate_na_id_number(gender):
    # Generate valid Namibian ID number
    birth_date = fake.date_of_birth().strftime("%y%m%d")  # Get birth date in YYMMDD format
    if gender == "Female":
        random_gender_digit = random.randint(0, 4) * 2 + 1  # Generate 1 random odd digit for females
    else:
        random_gender_digit = random.randint(0, 4) * 2  # Generate 1 random even digit for males
    random_digits = str(random.randint(0, 9999)).zfill(4)  # Generate 4 random digits

    id_number = birth_date + str(random_gender_digit) + random_digits

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

def generate_province():
    # Generate a random province from the list
    province = random.choice(sa_provinces)
    return province

def generate_region():
    # Generate a random region from the list
    region = random.choice(na_regions)
    return region

def generate_postal_code():
    # Generate a random postal code ranging from 0000 to 9999
    postal_code = str(random.randint(0, 9999)).zfill(4)
    return postal_code

data = []

# Loop through range up to 100
for val in range(100):
    gender = fake.random_element(["Female", "Male"])  # Randomly choose a gender
    item = {
        "ID": generate_sa_id_number(gender),  # Generate a unique and valid South African ID number based on gender
        "Name": fake.first_name_female() if gender == "Female" else fake.first_name_male(),
        "Lastname": fake.last_name(),
        "PhoneNumber": generate_phone_number(),  # Generate a phone number with 9 digits and no special characters
        "Country": "South Africa",  # Set the default country as South Africa
        "Text": fake.text(),
        "Date": fake.date(),
        "VisaCardNumber": generate_test_card_number("visa"),  # Generate a Visa test card number
        "MastercardNumber": generate_test_card_number("mastercard"),  # Generate a Mastercard test card number
        "AccountBalance": generate_account_balance(),  # Generate an account balance
        "Province": generate_province(),  # Generate a random province
        "PostalCode": generate_postal_code(),  # Generate a random postal code
        "Gender": gender,  # Add the gender to the item object
    }
    data.append(item)

    # Generate additional data item with Namibian ID number
    na_gender = "Female" if gender == "Female" else "Male"
    na_item = {
        "ID": generate_na_id_number(na_gender),  # Generate a unique and valid Namibian ID number based on gender
        "Name": fake.first_name_female() if na_gender == "Female" else fake.first_name_male(),
        "Lastname": fake.last_name(),
        "PhoneNumber": generate_phone_number(),  # Generate a phone number with 9 digits and no special characters
        "Country": "Namibia",  # Set the default country as Namibia
        # "Text": fake.text(),
        "Date": fake.date(),
        "VisaCardNumber": generate_test_card_number("visa"),  # Generate a Visa test card number
        "MastercardNumber": generate_test_card_number("mastercard"),  # Generate a Mastercard test card number
        "AccountBalance": generate_account_balance(),  # Generate an account balance
        "Region": generate_region(),  # Generate a random region in Namibia
        "PostalCode": generate_postal_code(),  # Generate a random postal code
        "Gender": na_gender,  # Add the gender to the item object
    }
    data.append(na_item)

# Write data to JSON file
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data written to output.json file.")
