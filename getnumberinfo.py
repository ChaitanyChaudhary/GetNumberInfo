# pip install phonenumbers

import phonenumbers
from phonenumbers import timezone 
from phonenumbers import geocoder, carrier, number_type


def get_number_type_mapping():
  return {
    0: 'FIXED_LINE',
    1: 'MOBILE',
    2: 'FIXED_LINE_OR_MOBILE',
    3: 'TOLL_FREE',
    4: 'PREMIUM_RATE',
    5: 'SHARED_COST',
    6: 'VOIP',
    7: 'PERSONAL_NUMBER',
    8: 'PAGER',
    9: 'UAN',
    10: 'VOICEMAIL',
    11: 'UNKNOWN'
  }


M_Number = input("Enter Mobile Number: ")

# Check M_Number is valid or not! & Get info.
def check_get_num(M_Number):

    try:
        # Parse the input as a phone number
        phoneNumber = phonenumbers.parse(M_Number, None)

        # Check if the parsed number is valid
        if phonenumbers.is_valid_number(phoneNumber):
            print(f"{M_Number} is a valid number\n")
            print("Here's your Phone Number details: \n")

            print(phoneNumber)
            print(f"Carrier: {carrier.name_for_number(phoneNumber, 'en')}")
            print(f"timeZone: {timezone.time_zones_for_number(phoneNumber)}")
            print(f"Region: {geocoder.description_for_number(phoneNumber, 'en')}")

            number_Type = phonenumbers.number_type(phoneNumber)
            # Get the mapping
            number_type_mapping = get_number_type_mapping()

            # Get the string representation
            type_string = number_type_mapping.get(number_Type, 'UNKNOWN')
            print(f"Number Type: {type_string}")

        else:
            print(
                f"{M_Number} is invalid \nPlease enter a valid phone number with country code\n"
            )

    except phonenumbers.NumberParseException as e:
        print(f"Error: {e}\n{M_Number} is invalid \nPlease enter a valid phone number with country code\n")


check_get_num(M_Number)