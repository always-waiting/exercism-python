import numpy as np
def saddle_points(a):
    if len(a) == 0:
        return set()
    a = np.array(a)
    maxes = np.empty_like(a)
    mins = np.empty_like(a)
    max_in_rows = np.max(a, axis=1)
    min_in_columns = np.min(a, axis=0)
    for i, row in enumerate(a):
        maxes[i] = row == max_in_rows[i]
    for i, col in enumerate(a.T):
        mins[i] = col == min_in_columns[i]
    return {(a, b) for (a, b) in zip(*np.nonzero(np.logical_and(maxes, mins.T)))}

