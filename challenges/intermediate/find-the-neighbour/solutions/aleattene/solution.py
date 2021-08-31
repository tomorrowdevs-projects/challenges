
"""
Python solution for challenge: "Find the neighbour"
To start the tests, type from CLI: python tests.py
"""

import re
import math


def find_neighbour(cube, query):
    # List containing the names (currently works only with the English alphabet)
    names_list = re.findall("[a-zA-Z]+", cube)
    # Length of the row (or column) of the cube
    row_len = int(math.sqrt(len(names_list)))
    # Data structure to manage the four search directions
    directions = {"left": -1, "right": +1, "upstairs": -row_len, "downstairs": +row_len}
    # Name and direction (taken from the input string)
    query_name, query_direction = re.findall("[a-zA-Z]+", query)[0:3:2]
    # Index of the query_name in the names_list
    index_name = names_list.index(query_name)
    # Index of the neighbor in the names_list
    index_neighbor = index_name + directions[query_direction]
    # Check if the index_neighbor is not correct (out of the extremes of the cube or not in the same row)
    if (query_direction in ['left', 'right'] and (index_name // row_len != index_neighbor // row_len)) \
            or not(0 <= index_neighbor <= len(names_list) - 1):
        return "nobody"
    # The index of the neighbor is correct and therefore, it is possible to return the real name.
    else:
        return names_list[index_neighbor]
