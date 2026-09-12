import pandas as pd
import random
import os

# Read products to get actual prices
products = pd.read_csv("../data/raw/products.csv")

price_lookup = dict(
    zip(products["ProductID"], products["Price"])
)

order_items = []

order_item_id = 1

# 200,000 Orders
for order_id in range(1, 200001):

    # Each order contains 1–4 products
    number_of_items = random.randint(1, 4)

    selected_products = random.sample(
        range(1, 1001),
        number_of_items
    )

    for product in selected_products:

        qty = random.randint(1, 5)

        price = float(price_lookup[product])

        discount = round(
            random.uniform(0, price * 0.15),
            2
        )

        order_items.append({

            "OrderItemID": order_item_id,
            "OrderID": order_id,
            "ProductID": product,
            "Quantity": qty,
            "UnitPrice": price,
            "Discount": discount

        })

        order_item_id += 1

df = pd.DataFrame(order_items)

output = "../data/raw/order_items.csv"

os.makedirs(os.path.dirname(output), exist_ok=True)

df.to_csv(output, index=False)

print("="*50)
print("Order Items Generated Successfully")
print(f"Total Records : {len(df)}")
print("="*50)