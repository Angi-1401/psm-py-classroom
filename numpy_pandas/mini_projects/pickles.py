# Given a Series called pickle, replace NaNs using the following algorithm:
#
# for each NaN:
#  get the nearest non NaN value before and after it
#  if both of those values exist:
#    replace NaN with the minimum of those two non NaN values
#  else:
#    replace NaN with the nearest non NaN value

import numpy as np
import pandas as pd

pickle = pd.Series(
    [
        1.5,
        np.nan,
        2.3,
        np.nan,
        np.nan,
        -3.9,
        np.nan,
        4.5,
        np.nan,
        np.nan,
        np.nan,
        1.9,
        np.nan,
    ]
)

for i in range(len(pickle)):
    if np.isnan(pickle[i]):
        nearest_before = np.nan
        nearest_after = np.nan

        if i == 0:
            nearest_after = pickle[i + 1]

        if i > 0 and i < len(pickle) - 1:
            nearest_before = pickle[i - 1]
            nearest_after = pickle[i + 1]

        if i == len(pickle) - 1:
            nearest_before = pickle[i - 1]

        if not np.isnan(nearest_before) and not np.isnan(nearest_after):
            pickle[i] = min(nearest_before, nearest_after)
        elif not np.isnan(nearest_before):
            pickle[i] = nearest_before
        elif not np.isnan(nearest_after):
            pickle[i] = nearest_after


print(pickle)
