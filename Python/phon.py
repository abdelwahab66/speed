import phonenumbers
from phonenumbers import geocoder, carrier, timezone

enter = input("please your phon num : ")

entered = phonenumbers.parse(enter, None)

print(entered)

local = geocoder.description_for_number(entered, "en")

print(local)

ser = carrier.name_for_number(entered, "en")

print(ser)

time = timezone.time_zones_for_number(entered)

print(time)
