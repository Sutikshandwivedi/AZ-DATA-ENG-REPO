from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

categories = [
    "Electronics",
    "Fashion",
    "Furniture",
    "Sports",
    "Grocery"
]

brands = {
    "Electronics": ["Apple", "Samsung", "Sony", "LG", "Dell"],
    "Fashion": ["Nike", "Adidas", "Puma", "Levis", "Zara"],
    "Furniture": ["IKEA", "Nilkamal", "Godrej"],
    "Sports": ["Yonex", "Nike", "Adidas", "Cosco"],
    "Grocery": ["Amul", "Tata", "Nestle", "Britannia"]
}

products = []

for i in range(1,1001):

    category = random.choice(categories)
    brand = random.choice(brands[category])

    products.append({
        "ProductID": i,
        "ProductName": fake.word().title() + " " + category[:3],
        "Category": category,
        "Brand": brand,
        "Price": round(random.uniform(100,50000),2),
        "CostPrice": round(random.uniform(50,30000),2),
        "IsActive": 1
    })

df = pd.DataFrame(products)

output_path = "../data/raw/products.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

df.to_csv(output_path,index=False)

print("="*50)
print("Products Generated Successfully")
print(f"Total Records : {len(df)}")
print("="*50)