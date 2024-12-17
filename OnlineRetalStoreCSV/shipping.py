import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Load the Orders data
orders_file = "/workspaces/OnlineRetailAnalysis/OnlineRetalStoreCSV/orders_data.csv"
orders = pd.read_csv(orders_file)

# Generate Shipping table
def generate_shipping(orders):
    carriers = ["FedEx", "DHL", "BlueDart", "India Post"]
    shipping_statuses = ["In Transit", "Delivered", "Pending"]

    shipping = []

    for _, order in orders.iterrows():
        carrier = random.choice(carriers)
        shipping_cost = round(random.uniform(50, 500), 2)  # Random shipping cost between 50 and 500
        status = random.choice(shipping_statuses)
        tracking_number = fake.uuid4()

        shipping.append({
            "ShippingID": f"SHIP{len(shipping) + 1}",
            "OrderID": order["OrderID"],
            "Carrier": carrier,
            "ShippingCost": shipping_cost,
            "ShippingStatus": status,
            "TrackingNumber": tracking_number
        })

    return pd.DataFrame(shipping)

# Generate the Shipping table
shipping_df = generate_shipping(orders)

# Save to CSV
output_file = "shipping_data.csv"
shipping_df.to_csv(output_file, index=False)
print(f"Shipping table with {len(shipping_df)} entries has been saved to {output_file}.")
