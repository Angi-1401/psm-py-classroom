# Define a person’s Family IQ Score as
# FamilyIQ = 0.5 * IQ + 0.5 * RelativesIQ
# where RelativesIQ is the average IQ score of that person’s parents, full siblings, and children.
# Given a dataset of people and their IQ scores, determine who has the highest FamilyIQ.

import numpy as np
import pandas as pd

generator = np.random.default_rng(2718)
persons = pd.DataFrame(
    {
        "id": [2, 3, 8, 12, 14, 15, 17, 32, 35, 41, 60, 64, 83, 98],
        "mom_id": [35, 41, pd.NA, 35, 41, 2, pd.NA, pd.NA, pd.NA, pd.NA, 8, 12, 35, 2],
        "dad_id": [
            17,
            8,
            pd.NA,
            17,
            8,
            32,
            pd.NA,
            pd.NA,
            pd.NA,
            pd.NA,
            pd.NA,
            14,
            17,
            14,
        ],
        "iq": np.round(generator.normal(loc=100, scale=20, size=14)),
    }
)

persons["siblings"] = None
persons["children"] = None

for index, person in persons.iterrows():
    siblings = persons[
        (persons["mom_id"] == person["mom_id"])
        & (persons["dad_id"] == person["dad_id"])
        & (persons["id"] != person["id"])
    ]

    children = persons[
        (persons["mom_id"] == person["id"]) | (persons["dad_id"] == person["id"])
    ]

    persons.at[index, "siblings"] = siblings["id"].tolist()
    persons.at[index, "children"] = children["id"].tolist()


persons["total_relatives"] = (
    persons["mom_id"].notna().astype(int)
    + persons["dad_id"].notna().astype(int)
    + persons["siblings"].apply(len)
    + persons["children"].apply(len)
)


persons["relatives_iq"] = (
    (
        persons["mom_id"].map(persons.set_index("id")["iq"]).fillna(0)
        + persons["dad_id"].map(persons.set_index("id")["iq"]).fillna(0)
        + persons["siblings"].apply(
            lambda siblings: (
                pd.Series(siblings).map(persons.set_index("id")["iq"]).mean()
                if siblings
                else 0
            )
        )
        + persons["children"].apply(
            lambda children: (
                pd.Series(children).map(persons.set_index("id")["iq"]).mean()
                if children
                else 0
            )
        )
    )
    / persons["total_relatives"]
).round(2)

persons["family_iq"] = (0.5 * persons["iq"] + 0.5 * persons["relatives_iq"]).round(2)

print(persons)
