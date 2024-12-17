import pandas as pd
import random

# Load the Orders and Products data
orders_file = "/workspaces/OnlineRetailAnalysis/OnlineRetalStoreCSV/orders_data.csv"
products_file = "/workspaces/OnlineRetailAnalysis/OnlineRetalStoreCSV/products_data.csv"

orders = pd.read_csv(orders_file)
products = pd.read_csv(products_file)

# Generate OrderDetails table
def generate_order_details(orders, products):
    order_details = []

    for _, order in orders.iterrows():
        num_items = random.randint(1, 3)  # Randomly decide the number of line items per order
        total_quantity = order["Quantity"]

        for _ in range(num_items):
            product = products.sample(1).iloc[0]
            
            # Split the quantity among items
            item_quantity = random.randint(1, total_quantity)
            total_quantity -= item_quantity
            if total_quantity < 0:
                item_quantity += total_quantity
                total_quantity = 0

            unit_price = product["Price"]
            total = round(item_quantity * unit_price, 2)

            order_details.append({
                "OrderDetailID": f"DETAIL{len(order_details) + 1}",
                "OrderID": order["OrderID"],
                "ProductID": product["ProductID"],
                "Quantity": item_quantity,
                "UnitPrice": unit_price,
                "Total": total
            })

            if total_quantity <= 0:
                break

    return pd.DataFrame(order_details)

# Generate the OrderDetails table
order_details_df = generate_order_details(orders, products)

# Save to CSV
output_file = "order_details.csv"
order_details_df.to_csv(output_file, index=False)
print(f"OrderDetails table with {len(order_details_df)} entries has been saved to {output_file}.")
