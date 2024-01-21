from faker import Faker
import csv

fake = Faker()
data = []
info = ["name", "job", "email", "phone", "country", "salary"]


def create(file, rows):
    with open(file, "w") as f:
        w = csv.DictWriter(f, fieldnames=info)
        w.writeheader()
        for i in range(int(rows)):
            data_dict = {}

            data_dict["name"] = fake.name()
            data_dict["job"] = fake.job()
            data_dict["email"] = fake.free_email()
            data_dict["phone"] = fake.phone_number()
            data_dict["country"] = fake.country()
            data_dict["salary"] = fake.random_int(min=3000, max=15000)
            data.append(data_dict)
        w.writerows(data)


name = input("name :  ")
num = input("row :  ")
create(name, num)
