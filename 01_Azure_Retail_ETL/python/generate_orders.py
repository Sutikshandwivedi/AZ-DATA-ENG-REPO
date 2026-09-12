from faker import Faker
import pandas as pd
import random
import os

fake = Faker("en_IN")

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Net Banking"
]

order_status = [
    "Delivered",
    "Delivered",
    "Delivered",
    "Shipped",
    "Processing",
    "Cancelled"
]

orders = []

for order_id in range(1, 200001):

    orders.append({
        "OrderID": order_id,

        "CustomerID": random.randint(1, 50000),

        "StoreID": random.randint(1, 50),

        "OrderDate": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),

        "OrderStatus": random.choice(order_status),

        "PaymentMethod": random.choice(payment_methods),

        "TotalAmount": round(
            random.uniform(200, 25000),
            2
        )
    })

df = pd.DataFrame(orders)

output_path = "../data/raw/orders.csv"

os.makedirs(os.path.dirname(output_path), exist_ok=True)

df.to_csv(output_path, index=False)

print("="*50)
print("Orders Generated Successfully")
print(f"Total Orders : {len(df)}")
print(f"Saved File   : {output_path}")
print("="*50)