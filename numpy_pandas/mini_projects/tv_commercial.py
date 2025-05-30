# You own a national restaurant chain called Applewasps. To increase sales, you decide to launch a multi-regional television marketing campaign.
# At the end of the campaign you have a table of commercials indicating when and where each commercial aired, and a table of sales indicating when and where customers generated sales.

import numpy as np
import pandas as pd

generator = np.random.default_rng(5555)
regions = ["north", "south", "east", "west"]

commercials = pd.DataFrame(
    {
        "commercial_id": range(10),
        "region": generator.choice(regions, size=10),
        "date_time": pd.to_datetime("2020-01-01")
        + pd.to_timedelta(generator.integers(240, size=10), unit="h"),
    }
)

sales = pd.DataFrame(
    {
        "sale_id": range(10),
        "region": generator.choice(regions, size=10),
        "date_time": pd.to_datetime("2020-01-01")
        + pd.to_timedelta(generator.integers(240, size=10), unit="h"),
        "revenue": np.round(generator.normal(loc=20, scale=5, size=10), 2),
    }
)

print(commercials)
print(sales)

# In order to analyze the performance of each commercial, map each sale to the commercial that aired prior to the sale, in the same region.

commercials = commercials.sort_values("date_time")
sales = sales.sort_values("date_time")

merged_data = pd.merge_asof(
    left=commercials, right=sales, on="date_time", by="region", direction="backward"
)
print(merged_data)
