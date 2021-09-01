import re
import numpy as np
from manager.query_utils import QueryUtils
from manager.cube import Cube

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


def find_neighbour(cube_str, query):
    cube_obj = Cube()
    if not cube_obj.load_cube(cube_str):
        return "Error, please check your input! \nYou have to pass a valid cube string:) "

    query_arguments = QueryUtils.parser(query)

    return cube_obj.get_neighbour(query_arguments)


print(find_neighbour(cubeStr, "Bob: My downstairs neighbor is (?)"))

print(find_neighbour(cubeStr, "Peter: My left neighbor is (?)"))  # == "Mike"
print(find_neighbour(cubeStr, "Bob: My upstairs neighbor is (?)"))  # == "Mike"
print(find_neighbour(cubeStr, "Tom: My right neighbor is (?)"))  # == "Jerry"
print(find_neighbour(cubeStr, "Jerry: My downstairs neighbor is (?)"))  # == "Peter"

# When there is no neighbour, return "nobody"

print(find_neighbour(cubeStr, "Wang: My right neighbor is (?)"))  # == "nobody"
print(find_neighbour(cubeStr, "Wang: My downstairs neighbor is (?)"))  # == "nobody"
print(find_neighbour(cubeStr, "Tom: My upstairs neighbor is (?)"))  # == "nobody"
