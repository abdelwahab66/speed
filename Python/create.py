from faker import Faker
import csv

fa = Faker()
data = []
details = ["name", "job", "phone", "email", "country", "salary"]


def create_file(file, rows):
    with open(file, "w") as f:
        w = csv.DictWriter(f, fieldnames=details)
        w.writeheader()
        for i in range(int(rows)):
            company_data = {}
            company_data["name"] = fa.name()
            company_data["job"] = fa.job()
            company_data["phone"] = fa.phone_number()
            company_data["email"] = fa.free_email()
            company_data["country"] = fa.country()
            company_data["salary"] = fa.random_int(min=3000, max=15000)
            data.append(company_data)
        w.writerows(data)


name = input("file name :  ")
row = input("num of rows : ")
create_file(name, row)
