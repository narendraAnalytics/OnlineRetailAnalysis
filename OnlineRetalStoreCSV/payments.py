import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Load the Orders data
orders_file = "/workspaces/OnlineRetailAnalysis/OnlineRetalStoreCSV/orders_data.csv"
orders = pd.read_csv(orders_file)

# Generate Payments table
def generate_payments(orders):
    payment_methods = ["Credit Card", "Debit Card", "PayPal", "Net Banking"]
    payment_statuses = ["Completed", "Pending", "Failed"]

    payments = []

    for _, order in orders.iterrows():
        payment_date = pd.to_datetime(order["OrderDate"]) + pd.Timedelta(days=random.randint(0, 3))
        payment_method = random.choice(payment_methods)
        payment_status = random.choice(payment_statuses)

        # Ensure realistic scenarios: Failed payments will not have an AmountPaid
        amount_paid = order["TotalAmount"] if payment_status == "Completed" else 0

        payments.append({
            "PaymentID": f"PAYMENT{len(payments) + 1}",
            "OrderID": order["OrderID"],
            "PaymentDate": payment_date,
            "PaymentMethod": payment_method,
            "PaymentStatus": payment_status,
            "AmountPaid": round(amount_paid, 2)
        })

    return pd.DataFrame(payments)

# Generate the Payments table
payments_df = generate_payments(orders)

# Save to CSV
output_file = "payments.csv"
payments_df.to_csv(output_file, index=False)
print(f"Payments table with {len(payments_df)} entries has been saved to {output_file}.")
