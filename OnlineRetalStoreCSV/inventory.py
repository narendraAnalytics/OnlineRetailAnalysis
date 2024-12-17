import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Load the Products and Suppliers data
products_file = "/workspaces/OnlineRetailAnalysis/OnlineRetalStoreCSV/products_data.csv"
suppliers_file = "/workspaces/OnlineRetailAnalysis/OnlineRetalStoreCSV/suppliers.csv"

products = pd.read_csv(products_file)
suppliers = pd.read_csv(suppliers_file)

# Generate Inventory table
def generate_inventory(products, suppliers):
    inventory = []

    for _, product in products.iterrows():
        supplier = suppliers.sample(1).iloc[0]
        restock_date = fake.date_between_dates(
            date_start=pd.to_datetime("2023-01-01"), date_end=pd.to_datetime("2024-12-31")
        )
        restock_quantity = random.randint(50, 500)  # Random restock quantity

        inventory.append({
            "InventoryID": f"INV{len(inventory) + 1}",
            "ProductID": product["ProductID"],
            "SupplierID": supplier["SupplierID"],
            "StockQuantity": product["StockQuantity"],
            "RestockDate": restock_date,
            "RestockQuantity": restock_quantity
        })

    return pd.DataFrame(inventory)

# Generate the Inventory table
inventory_df = generate_inventory(products, suppliers)

# Save to CSV
output_file = "inventory_data.csv"
inventory_df.to_csv(output_file, index=False)
print(f"Inventory table with {len(inventory_df)} entries has been saved to {output_file}.")
