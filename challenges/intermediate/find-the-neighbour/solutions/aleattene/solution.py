
"""
Python solution for challenge: "Find the neighbour"
To start the tests, type from CLI: python tests.py
"""


def find_neighbour(cube, query):
    # Data structures
    directions = {"left": -1, "right": +1, "upstairs": -3, "downstairs": +3}
    names_list = []
    # Creation of the list of names present in the cube
    for line in cube.split("|"):
        # Remove spaces at the beginning and at the end of the string
        line = line.strip()
        if line != "":
            if "A" <= line[0] <= "Z":
                names_list.append(line)
    # Name and direction (taken from the input string)
    query_name, query_direction = query.split(":")[0], query.split(" ")[2]
    # Index of the query_name in the names_list
    index_name = names_list.index(query_name)
    # Index of the neighbor in the names_list
    index_neighbor = index_name + directions[query_direction]
    # Query_direction is equal to left or right
    if query_direction in ['left', 'right']:
        # Check if the index_neighbor is correct (in the cube_lst and in the same row)
        if 0 <= index_neighbor <= len(names_list) - 1 and index_name // 3 == index_neighbor // 3:
            # Return the name of the neighbor
            return names_list[index_neighbor]
        else:
            # No neighbor
            return "nobody"
    # Query_direction is equal to upstairs or downstairs
    elif 0 <= index_neighbor <= len(names_list) - 1:
        # Return the name of the neighbor
        return names_list[index_neighbor]
    else:
        # No neighbor
        return "nobody"
