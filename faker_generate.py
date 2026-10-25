from faker import Faker
from random import randint
import json
from tqdm import tqdm

faker_data={}
fake = Faker()

for i in tqdm(range(5)):
    faker_employees=[]
    
    for i in tqdm(range(100000)):
        new_employee={
            "name": fake.first_name(),
            "job": fake.job(),
            "hourly_rate": randint(20,50),
            "weekly_hours_worked": randint(25,60),
            "contract_hours": randint(25,60)
        }
        faker_employees.append(new_employee)
    faker_data[fake.company()]=faker_employees


with open("data/faker.json", "w", encoding="utf-8") as fake_file:
    json.dump(faker_data, fake_file, indent=4, ensure_ascii=False)

    