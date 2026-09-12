from faker import Faker
import pandas as pd
import random
import os

# Indian fake data
fake = Faker("en_IN")

customers = []

for i in range(1, 50001):

    customers.append({
        "CustomerID": i,
        "FirstName": fake.first_name(),
        "LastName": fake.last_name(),
        "Gender": random.choice(["M", "F"]),
        "Email": fake.unique.email(),
        "Phone": fake.phone_number(),
        "City": fake.city(),
        "State": fake.state(),
        "CreatedDate": fake.date_between(
            start_date="-3y",
            end_date="today"
        )
    })

df = pd.DataFrame(customers)

# Save inside data/raw
output_path = "../data/raw/customers.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

df.to_csv(output_path, index=False)

print("="*50)
print("Customers Generated Successfully")
print(f"Total Records : {len(df)}")
print(f"Saved File    : {output_path}")
print("="*50)