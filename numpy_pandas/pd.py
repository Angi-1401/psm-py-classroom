import pandas as pd
import numpy as np

# Create a Serie in pandas
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=["a", "b", "c", "d", "e", "f"])
print(s)

# Accessing elements in pandas
print(s["a"])  # By label
print(s.iloc[3])  # By index

# Create a DataFrame

pets = pd.DataFrame(
    data={
        "name": [
            "Mr. Snuggles",
            "Honey Chew Chew",
            "Professor",
            "Chairman Meow",
            "Neighbelline",
        ],
        "type": ["cat", "dog", "dog", "cat", "horse"],
    },
    index=[71, 42, 11, 98, 42],
)

visits = pd.DataFrame(
    data={
        "pet_id": [42, 31, 71, 42, 98, 42],
        "date": [
            "2019-03-15",
            "2019-03-15",
            "2019-04-05",
            "2019-04-06",
            "2019-04-12",
            "2019-04-12",
        ],
    }
)

# Merge visits and pets
print(pd.merge(left=pets, right=visits, how="left", left_index=True, right_on="pet_id"))
