import phonenumbers
from phonenumbers import geocoder

phone_number = phonenumbers.parse('+79801131352')

print(geocoder.description_for_number(phone_number, 'ru'))
