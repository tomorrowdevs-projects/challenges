import re


def find_neighbour(cube: str, query: str) -> str:
    # transform the string cube in names list using regex
    people_in_cube = re.findall("[a-zA-Z]+", cube)

    # convert the names list to a single tmp string with | separator
    who_am_i = '|'.join(people_in_cube)

    # find my name in query (without using slices isn't important if the string structure changes)
    my_name = ''.join(re.findall(f"{who_am_i}+", query))

    # find my position in the cube, if I'm in the cube
    if my_name != '':
        me = people_in_cube.index(my_name)
    else:
        return 'Name entered not found'

    # how many places I have to shift to find my neighbor?
    directions = {'right': 1, 'left': -1, 'downstairs': 3, 'upstairs': -3}

    # convert the directions keys to a single tmp string with | separator
    where_i_go = '|'.join(directions)

    # find my direction in query (without using slices isn't important if the string structure changes)
    towards = ''.join(re.findall(f"{where_i_go}", query))

    # find the index to check in the cube
    move = me + directions[towards]

    # if the index is in the cube, find the neighbor, else return nobody
    return people_in_cube[move] if 0 <= move <= (len(people_in_cube) - 1) else 'nobody'


cubeStr = """
   ______________________
  /_____________________/|
 /_____________________/ |
 |      |      |      |  |
 | Tom  |Jerry | John | /|
 |______|______|______|/ |
 |      |      |      |  |
 | Mike |Peter |Alice | /|
 |______|______|______|/ |
 |      |      |      |  |
 |  Bob | Bill | Wang | /
 |______|______|______|/
"""

# Test cases

print(find_neighbour(cubeStr, "Peter: My left neighbor is (?)"))  # "Mike"
print(find_neighbour(cubeStr, "Bob: My upstairs neighbor is (?)"))  # "Mike"
print(find_neighbour(cubeStr, "Tom: My right neighbor is (?)"))  # "Jerry"
print(find_neighbour(cubeStr, "Jerry: My downstairs neighbor is (?)"))  # "Peter"

# When there is no neighbour, return "nobody"

print(find_neighbour(cubeStr, "Wang: My right neighbor is (?)"))  # "nobody"
print(find_neighbour(cubeStr, "Wang: My downstairs neighbor is (?)"))  # "nobody"
print(find_neighbour(cubeStr, "Tom: My upstairs neighbor is (?)"))  # "nobody"
