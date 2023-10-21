import json
from faker import Faker
import random
from datetime import datetime

# Initialize Faker
fake = Faker1()
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
    birth_year_suffix = datetime.now().year % 100  # Get the current year suffix (YY format)
    birth_month = random.randint(1, 12)  # Generate a random birth month
    birth_day = random.randint(1, 28)  # Generate a random birth day
    if gender == "Female":
        random_gender_digits = str(random.randint(0, 4999)).zfill(4)  # Generate 4 random digits for females
    else:
        random_gender_digits = str(random.randint(5000, 9999)).zfill(4)  # Generate 4 random digits for males
    citizenship = random.randint(0, 1)  # Generate 1 digit for citizenship (either 0 or 1)
    checksum = str(random.randint(0, 99)).zfill(2)  # Generate 2 digits for checksum

    id_number = f"{birth_year_prefix:02}{birth_month:02}{birth_day:02}{random_gender_digits}{citizenship}{checksum}"
    
    is_citizen = True if citizenship == 0 else False

    # Calculate the age based on the first 6 digits (YYMMDD) of the ID number
    birth_date_str = id_number[:6]
    birth_date_obj = datetime.strptime(birth_date_str, "%y%m%d")
    today = datetime.today()
    age = today.year - birth_date_obj.year
    
    # Adjust the age if the birthday hasn't occurred yet this year
    if today.month < birth_date_obj.month or (today.month == birth_date_obj.month and today.day < birth_date_obj.day):
        age -= 1

    return id_number, is_citizen, age

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
    id_number, is_citizen, age = generate_sa_id_number(gender)
    item = {
        "ID": id_number,  # Generate a unique and valid South African ID number based on gender
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
        "Gender": gender,  # Add the gender to the item object
        "isCitizen": is_citizen,  # Add the isCitizen boolean field
        "Age": age  # Add the age field
    }
    data.append(item)

# Write data to JSON file
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data written to output.json file.")
