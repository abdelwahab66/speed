from faker import Faker

f = Faker()
# names
print("name: " + f.name_female())
print("first name: " + f.first_name())
print("last name: " + f.last_name())

# email
print("email : " + f.email())
print("free email : " + f.free_email())
print("company email : " + f.company_email())

# address
print("address :  " + f.address())
print("country :  " + f.country())
print("current country :  " + f.current_country())
print("city :  " + f.city())
print("street name :  " + f.street_name())
print("building number :  " + f.building_number())
print("post code :  " + f.postcode())

print("________________")

# c.c
print(f.credit_card_full())
print("credit card provider :  " + f.credit_card_provider())
print("credit card name :  " + f.name())
print("credit card expire :  " + f.credit_card_expire())
print("credit card number :  " + f.credit_card_number())
print("credit card number visa :  " + f.credit_card_number(card_type="visa"))
print(
    "credit card number mastercard :  " + f.credit_card_number(card_type="mastercard")
)
print("credit card cvc :  " + f.credit_card_security_code())
