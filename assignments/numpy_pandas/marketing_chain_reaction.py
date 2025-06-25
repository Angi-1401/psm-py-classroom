# You work for a retail chain. Each marketing email campaign is tracked, and sales are logged by customer ID and timestamp.

import numpy as np
import pandas as pd

np.random.seed(42)

emails = pd.DataFrame(
    {
        "email_id": range(6),
        "customer_id": [101, 102, 103, 101, 104, 105],
        "send_time": pd.to_datetime("2023-01-01")
        + pd.to_timedelta(np.random.randint(0, 240, size=6), unit="h"),
    }
)

sales = pd.DataFrame(
    {
        "sale_id": range(6),
        "customer_id": [101, 102, 101, 104, 106, 105],
        "sale_time": pd.to_datetime("2023-01-01")
        + pd.to_timedelta(np.random.randint(0, 240, size=6), unit="h"),
        "amount": np.round(np.random.normal(100, 20, size=6), 2),
    }
)

print("Emails:")
print(emails)
print("Sales:")
print(sales)

# For each sale, determine if it occurred within 72 hours after the customer received a marketing email. Flag it as "influenced" if so.

# Sort for merge_asof
emails_sorted = emails.sort_values("send_time")
sales_sorted = sales.sort_values("sale_time")

# Match each sale with most recent prior email to the same customer
merged = pd.merge_asof(
    left=sales_sorted,
    right=emails_sorted,
    by="customer_id",
    left_on="sale_time",
    right_on="send_time",
    direction="backward",
)

# Check if sale is within 72 hours of the matched email
merged["influenced"] = (merged["sale_time"] - merged["send_time"]) <= pd.Timedelta(
    "72h"
)

print("Merged result with influence flag:")
print(merged[["sale_id", "customer_id", "sale_time", "send_time", "influenced"]])
