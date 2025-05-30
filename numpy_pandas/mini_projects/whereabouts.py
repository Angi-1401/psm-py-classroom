# You track the whereabouts of 100 individuals in a DataFrame called whereabouts. Each person has a corresponding list of place ids indicating the places they’ve visited in the recent week. You also track which places have been exposed to COVID-19 in a list called exposed 😷.

import numpy as np
import pandas as pd

# exposed places
exposed = [0, 5, 9]

# whereabouts of each person
generator = np.random.default_rng(2468)
n_places = 10
n_persons = 10
place_ids = np.arange(n_places)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
visits = generator.choice(place_ids, size=3 * n_places, replace=True)
split_idxs = np.sort(generator.choice(len(visits), size=9, replace=True))
whereabouts = pd.DataFrame(
    {
        "person_id": range(n_persons),
        "places": [np.unique(x).tolist() for x in np.array_split(visits, split_idxs)],
    }
)
print(whereabouts)

# For each person, identify the places they visited which have been exposed. Make this a new list-column in whereabouts called exposures

whereabouts["exposures"] = whereabouts["places"].apply(
    lambda places: [place for place in places if place in exposed]
)

# If a person has visited all of the exposed places, mark his as infected

whereabouts["infected"] = whereabouts["exposures"].apply(
    lambda exposures: len(exposures) == len(exposed)
)

print(whereabouts)
