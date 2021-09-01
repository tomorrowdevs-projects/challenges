import re
import numpy as np


class Cube:

    def __init__(self):
        self.cube = None

    # Load cube string to a cube obj
    # @ return ->
    # ----------> True if passed string is valid
    # ----------> False if passed string is NOT valid
    def load_cube(self, cube_str) -> 'bool':

        cube_str = cube_str.lower()

        # Extract (with regex) elements from the cube string
        regex = r"(?=\w)[a-zA-Z]+(?<=\w)"
        elements = re.findall(regex, cube_str)

        # check if the passed cube string is valid
        sqrt = len(elements) ** (1 / 2)
        if int(sqrt + 0.5) ** 2 != len(elements):
            # passed string isn't a cube!
            return False

        # add string elements to numpy 2nd array
        self.cube = np.array(elements).reshape(int(sqrt), int(sqrt))

        return True

    # Return the neighbour list
    # @ parameters ->
    # @ ------------> arguments: dict as formatted {'name': started name, 'command_key': [0,1,2,3]}
    # @ return -> name of neighbour
    def get_neighbour(self, arguments):

        name = str(arguments['name'][0]).lower()

        command = arguments['command_key'][0]

        if command == -1:
            return "Bad command"

        index = np.where(self.cube == name)

        # name not found
        if len(index[0]) == 0:
            return "Name not found"

        def right_of(start_index):
            if start_index[1] == len(self.cube) - 1:
                return [0]
            return self.cube[start_index[0], start_index[1] + 1]

        def left_of(start_index):
            if start_index[1] == 0:
                return [0]
            return self.cube[start_index[0], start_index[1] - 1]

        def upstairs_of(start_index):
            if start_index[0] == 0:
                return [0]
            return self.cube[start_index[0] - 1, start_index[1]]

        def downstairs_of(start_index):
            if start_index[0] == len(self.cube) - 1:
                return [0]

            return self.cube[start_index[0] + 1, start_index[1]]

        commands_list = {
            0: right_of,
            1: left_of,
            2: upstairs_of,
            3: downstairs_of
        }
        result = commands_list[command](index)

        if result[0] == 0:
            return "Nobody"
        else:
            return result
