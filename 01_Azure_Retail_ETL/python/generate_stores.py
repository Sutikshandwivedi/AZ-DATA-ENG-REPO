from faker import Faker
import pandas as pd
import random
import os

fake = Faker("en_IN")

regions = {
    "North": ["Delhi", "Punjab", "Haryana", "Uttar Pradesh"],
    "South": ["Karnataka", "Tamil Nadu", "Kerala", "Telangana"],
    "West": ["Maharashtra", "Gujarat", "Rajasthan", "Goa"],
    "East": ["West Bengal", "Odisha", "Bihar", "Jharkhand"]
}

store_types = ["Mall", "High Street", "Franchise", "Retail Hub"]

stores = []

store_id = 1

for region, states in regions.items():

    for state in states:

        for _ in range(3):

            stores.append({
                "StoreID": store_id,
                "StoreName": f"RetailKart Store {store_id}",
                "StoreType": random.choice(store_types),
                "City": fake.city(),
                "State": state,
                "Region": region,
                "OpenDate": fake.date_between(start_date="-8y", end_date="-6m"),
                "IsActive": random.choice([1,1,1,1,0])
            })

            store_id += 1

while len(stores) < 50:

    stores.append({
        "StoreID": store_id,
        "StoreName": f"RetailKart Store {store_id}",
        "StoreType": random.choice(store_types),
        "City": fake.city(),
        "State": fake.state(),
        "Region": random.choice(list(regions.keys())),
        "OpenDate": fake.date_between(start_date="-8y", end_date="-6m"),
        "IsActive": 1
    })

    store_id += 1

df = pd.DataFrame(stores)

output_path = "../data/raw/stores.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

df.to_csv(output_path, index=False)

print("="*50)
print("Stores Generated Successfully")
print(f"Total Records : {len(df)}")
print("="*50)