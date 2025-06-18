#Write a regular expression to validate a phone number.

import re

pattern = r'^[6789]\d{9}$'

phone_number = input("Enter your phone number: ")

if re.match(pattern, phone_number):
    print("Valid phone number")
else:
    print("Invalid phone number")
