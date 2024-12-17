import random
import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker("en_IN")

# Number of stores and suppliers
num_stores = 10
num_suppliers = 100

# Generate StoreDetails table
def generate_store_details(num_stores):
    store_data = {
        "StoreID": [f"STORE{i+1}" for i in range(num_stores)],
        "StoreName": [fake.company() for _ in range(num_stores)],
        "Location": [f"{fake.city()}, {fake.state()}" for _ in range(num_stores)],
        "Manager": [fake.name() for _ in range(num_stores)],
        "OpeningDate": [fake.date_between_dates(date_start=pd.to_datetime("2000-01-01"), date_end=pd.to_datetime("2024-01-01")) for _ in range(num_stores)],
        "ContactNumber": [fake.phone_number() for _ in range(num_stores)]
    }
    return pd.DataFrame(store_data)

# Generate Suppliers table
def generate_suppliers(num_suppliers):
    supplier_data = {
        "SupplierID": [f"SUPPLIER{i+1}" for i in range(num_suppliers)],
        "SupplierName": [fake.company() for _ in range(num_suppliers)],
        "ContactNumber": [fake.phone_number() for _ in range(num_suppliers)],
        "Email": [fake.email() for _ in range(num_suppliers)],
        "City": [fake.city() for _ in range(num_suppliers)],
        "State": [fake.state() for _ in range(num_suppliers)]
    }
    return pd.DataFrame(supplier_data)

# Generate and save the StoreDetails table
store_details_df = generate_store_details(num_stores)
store_output_file = "store_details.csv"
store_details_df.to_csv(store_output_file, index=False)
print(f"StoreDetails table with {num_stores} stores has been saved to {store_output_file}.")

# Generate and save the Suppliers table
suppliers_df = generate_suppliers(num_suppliers)
suppliers_output_file = "suppliers.csv"
suppliers_df.to_csv(suppliers_output_file, index=False)
print(f"Suppliers table with {num_suppliers} suppliers has been saved to {suppliers_output_file}.")
