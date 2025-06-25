# You’re analyzing household purchase behavior across multiple people in the same household.

import numpy as np
import pandas as pd

np.random.seed(281)

people = pd.DataFrame({"person_id": range(1, 7), "household_id": [1, 1, 2, 2, 3, 3]})

purchases = pd.DataFrame(
    {
        "purchase_id": range(10),
        "person_id": np.random.choice(people["person_id"], size=10),
        "amount": np.round(np.random.normal(50, 10, size=10), 2),
    }
)

print("People:")
print(people)
print("Purchases:")
print(purchases)

# Calculate a “Household Spending Score” as the average revenue per person per household.

# Map household_id to purchases
purchases["household_id"] = purchases["person_id"].map(
    people.set_index("person_id")["household_id"]
)

# Total household revenue
total_by_household = purchases.groupby("household_id")["amount"].sum()

# Number of people per household
people_count = people.groupby("household_id")["person_id"].nunique()

# Compute spending score
household_spending = (
    (total_by_household / people_count)
    .rename("household_spending_score")
    .round(2)
    .reset_index()
)

print("\nHousehold Spending Score (per person):")
print(household_spending)
