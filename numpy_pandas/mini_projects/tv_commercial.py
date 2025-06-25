import numpy as np
import pandas as pd

generator = np.random.default_rng(5555)
regions = ["north", "south", "east", "west"]

# Generate sample commercials
commercials = pd.DataFrame(
    {
        "commercial_id": range(10),
        "region": generator.choice(regions, size=10),
        "date_time": pd.to_datetime("2020-01-01")
        + pd.to_timedelta(generator.integers(240, size=10), unit="h"),
    }
)

# Generate sample sales
sales = pd.DataFrame(
    {
        "sale_id": range(10),
        "region": generator.choice(regions, size=10),
        "date_time": pd.to_datetime("2020-01-01")
        + pd.to_timedelta(generator.integers(240, size=10), unit="h"),
        "revenue": np.round(generator.normal(loc=20, scale=5, size=10), 2),
    }
)

print("Commercials:")
print(commercials)
print("\nSales:")
print(sales)

# Map each sale to the most recent commercial in the same region before the sale
sales_sorted = sales.sort_values("date_time")
commercials_sorted = commercials.sort_values("date_time")

sales_with_commercials = pd.merge_asof(
    left=sales_sorted,
    right=commercials_sorted,
    on="date_time",
    by="region",
    direction="backward",
)

print("\nSales with matched commercials:")
print(sales_with_commercials)
