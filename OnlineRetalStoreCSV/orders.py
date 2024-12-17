import random
import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Load existing datasets
customers = pd.read_csv("/workspaces/OnlineRetailAnalysis/OnlineRetalStoreCSV/customers.csv")
products = pd.read_csv("/workspaces/OnlineRetailAnalysis/OnlineRetalStoreCSV/products_data.csv")
stores = pd.read_csv("/workspaces/OnlineRetailAnalysis/OnlineRetalStoreCSV/store_details.csv")

# Number of orders to generate
num_orders = 20000

# Generate Orders table
def generate_orders(customers, products, stores, num_orders):
    orders = []

    for _ in range(num_orders):
        customer = customers.sample(1).iloc[0]
        product = products.sample(1).iloc[0]
        store = stores.sample(1).iloc[0]

        order_date = fake.date_between_dates(
            date_start=pd.to_datetime("2022-01-01"), date_end=pd.to_datetime("2024-12-25")
        )
        delivery_date = order_date + pd.Timedelta(days=random.randint(2, 10))
        actual_delivery_date = delivery_date + pd.Timedelta(days=random.choice([-1, 0, 1]))

        quantity = random.randint(1, 10)
        total_amount = round(product["Price"] * quantity, 2)

        orders.append({
            "OrderID": f"ORDER{len(orders) + 1}",
            "CustomerID": customer["CustomerID"],
            "ProductID": product["ProductID"],
            "StoreID": store["StoreID"],
            "OrderDate": order_date,
            "DeliveryDate": delivery_date,
            "ActualDeliveryDate": actual_delivery_date,
            "Quantity": quantity,
            "TotalAmount": total_amount
        })

    return pd.DataFrame(orders)

# Generate the data
orders_df = generate_orders(customers, products, stores, num_orders)

# Save to CSV
output_file = "orders_data.csv"
orders_df.to_csv(output_file, index=False)
print(f"Orders table with {num_orders} entries has been saved to {output_file}.")
