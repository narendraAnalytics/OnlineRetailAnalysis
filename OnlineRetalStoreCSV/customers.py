import random
import pandas as pd
from faker import Faker

# Initialize Faker and set locale for Indian cities
fake = Faker("en_IN")

# Define the number of customers
num_customers = 8000

# Define the date range
start_date = pd.to_datetime("2022-01-01")
end_date = pd.to_datetime("2024-12-25")

# Define Indian cities
indian_cities = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai",
    "Kolkata", "Pune", "Jaipur", "Surat", "Lucknow", "Kanpur", "Nagpur",
    "Indore", "Thane", "Bhopal", "Visakhapatnam", "Pimpri-Chinchwad", "Patna",
    "Vadodara", "Ghaziabad", "Ludhiana", "Agra", "Nashik", "Faridabad",
    "Meerut", "Rajkot", "Varanasi", "Srinagar", "Aurangabad"
]

# Generate customer data
data = {
    "CustomerID": [f"CUST{i+1}" for i in range(num_customers)],
    "Name": [fake.name() for _ in range(num_customers)],
    "Email": [fake.email() for _ in range(num_customers)],
    "Phone": [fake.phone_number() for _ in range(num_customers)],
    "City": [random.choice(indian_cities) for _ in range(num_customers)],
    "RegistrationDate": [
        fake.date_between_dates(date_start=start_date, date_end=end_date) for _ in range(num_customers)
    ],
    "Gender": [random.choice(["Male", "Female"]) for _ in range(num_customers)],
    "Age": [random.randint(18, 64) for _ in range(num_customers)]
}

# Create DataFrame
customers_df = pd.DataFrame(data)

# Save to CSV
output_file = "customers.csv"
customers_df.to_csv(output_file, index=False)

print(f"Generated data for {num_customers} customers and saved to {output_file}.")

# In GitHub Codespaces Terminal:
# 1. Install necessary packages:
#    ```bash
#    pip install pandas faker
#    ```
# 2. Run the Python script:
#    ```bash
#    python generate_customers_data.py
#    ```
