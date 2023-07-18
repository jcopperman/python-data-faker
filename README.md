# python-data-faker
Python script for generating fake data for testing using [Faker](https://faker.readthedocs.io/en/master/) including valid SA & Namabian ID numbers, VISA and Mastercard test credit card numbers and formatted South African phone numbers, provinces and regions (region dependant, returns null).

Generates 100 each of SA and Namabian test objects into JSON

```
{
        "ID": "7806267991162",
        "Name": "Michael",
        "Lastname": "James",
        "PhoneNumber": "700714652",
        "Country": "South Africa",
        "Date": "2003-01-31",
        "VisaCardNumber": "4059562103399821",
        "MastercardNumber": "2624097595466531",
        "AccountBalance": 3646.62,
        "Province": "Northern Cape",
        "Region": null,
        "PostalCode": "8530",
        "Gender": "Male"
    },
    {
        "ID": "46051408193",
        "Name": "Adam",
        "Lastname": "Edwards",
        "PhoneNumber": "418903899",
        "Country": "Namibia",
        "Date": "1995-02-20",
        "VisaCardNumber": "4545427208633742",
        "MastercardNumber": "2226968799778750",
        "AccountBalance": 1922.57,
        "Province": null,
        "Region": "Ohangwena",
        "PostalCode": "5616",
        "Gender": "Male"
    },
```

## Pre-requisites
- Version: `Python 3.11.2`
- [Python installation guide](https://wiki.python.org/moin/BeginnersGuide/Download) 
- Install faker with `pip install faker`

## Usage
- Run script with `python faker.py` - outputs JSON file `output.json` with generated data
