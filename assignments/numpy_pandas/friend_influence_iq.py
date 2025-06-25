# You’re analyzing how much a person’s friends might influence their IQ.

import pandas as pd

people = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5],
        "iq": [105, 98, 110, 95, 100],
        "friends": [[2, 3], [1], [1, 5], [], [3]],
    }
)

print("People:")
print(people)

# For each person, compute the average IQ of their friends (if any), and define:
# SocialIQ = 0.7 * IQ + 0.3 * FriendsIQ

# Map friends to people
people["friends_iq"] = people["friends"].apply(
    lambda friends: pd.Series(friends).map(people.set_index("id")["iq"]).mean()
)

# Calculate Social IQ
people["social_iq"] = 0.7 * people["iq"] + 0.3 * people["friends_iq"]

print("\nPeople with Social IQ:")
print(people)
