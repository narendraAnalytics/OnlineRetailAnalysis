import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Load the Orders and Products data
orders_file = "/workspaces/OnlineRetailAnalysis/OnlineRetalStoreCSV/orders_data.csv"
products_file = "/workspaces/OnlineRetailAnalysis/OnlineRetalStoreCSV/products_data.csv"

orders = pd.read_csv(orders_file)
products = pd.read_csv(products_file)

# Generate Returns table
def generate_returns(orders, products):
    return_reasons = ["Defective", "Wrong Item", "Not as Described", "Changed Mind"]
    return_statuses = ["Accepted", "Rejected"]

    returns = []

    for _, order in orders.sample(frac=0.2).iterrows():  # Randomly select 20% of orders for returns
        product = products.loc[products["ProductID"] == order["ProductID"]].iloc[0]
        return_date = pd.to_datetime(order["ActualDeliveryDate"]) + pd.Timedelta(days=random.randint(1, 15))
        reason = random.choice(return_reasons)
        status = random.choice(return_statuses)

        # Refund amount depends on the status
        refund_amount = order["TotalAmount"] if status == "Accepted" else 0

        returns.append({
            "ReturnID": f"RETURN{len(returns) + 1}",
            "OrderID": order["OrderID"],
            "ProductID": order["ProductID"],
            "ReturnDate": return_date,
            "Reason": reason,
            "Status": status,
            "RefundAmount": round(refund_amount, 2)
        })

    return pd.DataFrame(returns)

# Generate the Returns table
returns_df = generate_returns(orders, products)

# Save to CSV
output_file = "returns_data.csv"
returns_df.to_csv(output_file, index=False)
print(f"Returns table with {len(returns_df)} entries has been saved to {output_file}.")
