import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Load the Customers and Products data
customers_file = "/workspaces/OnlineRetailAnalysis/OnlineRetalStoreCSV/customers.csv"
products_file = "/workspaces/OnlineRetailAnalysis/OnlineRetalStoreCSV/products_data.csv"

customers = pd.read_csv(customers_file)
products = pd.read_csv(products_file)

# Generate Reviews and Ratings table
def generate_reviews_and_ratings(customers, products):
    reviews = []

    for _ in range(len(customers) // 2):  # Assume 50% of customers leave reviews
        customer = customers.sample(1).iloc[0]
        product = products.sample(1).iloc[0]

        review_date = fake.date_between_dates(
            date_start=pd.to_datetime(customer["RegistrationDate"]),
            date_end=pd.to_datetime("2024-12-31")
        )
        rating = random.randint(1, 5)  # Ratings between 1 and 5 stars
        review_text = fake.sentence(nb_words=random.randint(10, 20))

        reviews.append({
            "ReviewID": f"REVIEW{len(reviews) + 1}",
            "CustomerID": customer["CustomerID"],
            "ProductID": product["ProductID"],
            "Rating": rating,
            "ReviewText": review_text,
            "ReviewDate": review_date
        })

    return pd.DataFrame(reviews)

# Generate the Reviews and Ratings table
reviews_df = generate_reviews_and_ratings(customers, products)

# Save to CSV
output_file = "reviews_ratings_data.csv"
reviews_df.to_csv(output_file, index=False)
print(f"Reviews and Ratings table with {len(reviews_df)} entries has been saved to {output_file}.")
