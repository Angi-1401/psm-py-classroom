# You polled five heterosexual couples on their hobbies.

import numpy as np
import pandas as pd

couples = pd.DataFrame(
    {
        "man": [
            ["fishing", "biking", "reading"],
            ["hunting", "mudding", "fishing"],
            ["reading", "movies", "running"],
            ["running", "reading", "biking", "mudding"],
            ["movies", "reading", "yodeling"],
        ],
        "woman": [
            ["biking", "reading", "movies"],
            ["fishing", "drinking"],
            ["knitting", "reading"],
            ["running", "biking", "fishing", "movies"],
            ["movies"],
        ],
    }
)

# For each couple, determine what hobbies each man has that his wife doesn’t and what hobbies each woman has that her husband doesn’t.


# Function to compute set differences
def unique_hobbies(row):
    man_hobbies = set(row["man"])
    woman_hobbies = set(row["woman"])
    return pd.Series(
        {
            "man_unique": list(man_hobbies - woman_hobbies),
            "woman_unique": list(woman_hobbies - man_hobbies),
        }
    )


# Apply function row-wise
unique_hobbies_df = couples.apply(unique_hobbies, axis=1)

# Combine results with original couples DataFrame if needed
result = couples.join(unique_hobbies_df)
print(result)
