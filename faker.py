import json
from faker import Faker
import random
import datetime

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
    birth_year_prefix = random.randint(0, 99)  # Generate a random birth year prefix (YY format)
    birth_year_suffix = datetime.datetime.now().year % 100  # Get the current year suffix (YY format)
    birth_month = random.randint(1, 12)  # Generate a random birth month
    birth_day = random.randint(1, 28)  # Generate a random birth day
    if gender == "Female":
        random_gender_digits = str(random.randint(0, 4999)).zfill(4)  # Generate 4 random digits for females
    else:
        random_gender_digits = str(random.randint(5000, 9999)).zfill(4)  # Generate 4 random digits for males
    citizenship = str(random.randint(0, 1)).zfill(1)  # Generate 1 digits for (Either 0 or 1)
    checksum = str(random.randint(0, 99)).zfill(2)  # Generate 2 digits for checksum

    id_number = f"{birth_year_prefix:02}{birth_month:02}{birth_day:02}{random_gender_digits}{citizenship}{checksum}"

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
        "Date": fake.date(),
        "VisaCardNumber": generate_test_card_number("visa"),  # Generate a Visa test card number
        "MastercardNumber": generate_test_card_number("mastercard"),  # Generate a Mastercard test card number
        "AccountBalance": generate_account_balance(),  # Generate an account balance
        "Province": generate_province(),  # Generate a random province
        "PostalCode": generate_postal_code(),  # Generate a random postal code
        "Gender": gender  # Add the gender to the item object
    }
    id_number = item["ID"]
    birth_year_prefix = int(id_number[:2])
    birth_year_suffix = datetime.datetime.now().year % 100
    birth_year = birth_year_prefix + birth_year_suffix
    birth_month = int(id_number[2:4])
    birth_day = int(id_number[4:6])
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    current_day = datetime.datetime.now().day
    birth_date = datetime.date(birth_year, birth_month, birth_day)
    age = current_year - birth_year
    if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
        age -= 1
    item["Age"] = age if age > 0 and age <= 120 else None
    data.append(item)

# Write data to JSON file
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data written to output.json file.")
