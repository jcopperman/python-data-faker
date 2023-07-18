
from faker import Faker
import json

#Intiaize Faker
fake = Faker()

fake.name()
'John'
fake.last_name()
'Doe'
fake.country()
'South Africa'
fake.text()
'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.'
fake.email()
'myfakemail@example.org'
fake.date()
'1985-01-06'
fake.phone_number()
'081 6054545'

#Loop through range up to 100
for val in range(100):
    y= json.dumps((f"Name: {fake.name()} Lastname: {fake.last_name()} PhoneNumber: {fake.phone_number()} Country: {fake.country()} Text: {fake.text()} Date: {fake.date()}"))
    print(y)
