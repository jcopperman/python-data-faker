from faker import Faker
import json

# Initialize Faker
fake = Faker()

data = []

# Loop through range up to 100
for val in range(100):
    item = {
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
