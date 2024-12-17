import random
import pandas as pd

# Load the provided product data
file_path = "/workspaces/OnlineRetailAnalysis/OnlineRetalStoreCSV/Product_Information_List.csv"
product_data = pd.read_csv(file_path)

# Drop unnecessary columns (e.g., unnamed index columns)
product_data = product_data.loc[:, ~product_data.columns.str.contains('^Unnamed')]

# Add additional fields for the Products table
product_data["ProductID"] = [f"PROD{i+1}" for i in range(len(product_data))]
product_data["Price"] = [round(random.uniform(50, 2000), 2) for _ in range(len(product_data))]  # Random price between 50 and 2000
product_data["StockQuantity"] = [random.randint(10, 500) for _ in range(len(product_data))]  # Random stock levels between 10 and 500

# Reorganize columns
product_data = product_data[["ProductID", "product_name", "category", "brand", "Price", "StockQuantity"]]

# Save the Products table to a new CSV file
output_file = "products_data.csv"
product_data.to_csv(output_file, index=False)

print(f"Products table with {len(product_data)} entries has been generated and saved to {output_file}.")
