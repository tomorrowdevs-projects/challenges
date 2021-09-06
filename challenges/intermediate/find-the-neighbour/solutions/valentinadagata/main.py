import re
from math import sqrt


def find_neighbour(cube, query):
    # delete all characters that are not letters
    regex = re.compile('[^a-zA-Z]')
    newcube = regex.sub(' ', cube)
    # transform the string to list
    newcube = newcube.split()
    # count how many rows and cols there are (so that it could be scalable)
    rows_cols = int(sqrt(len(newcube)))
    # transform the list into a matrix
    matrix = [newcube[x:x + rows_cols] for x in range(0, len(newcube), rows_cols)]

    # split the query to take the person name and the direction
    # use strip() to remove white spaces
    split_query = query.strip().split(":")
    person = split_query[0]
    split_direction = re.split(': | ', split_query[1].strip())
    direction = split_direction[1]

    """
    for each row and each column check the person and then extract the name of the neighbour from the matrix
    # upstairs == same column, previous row
    # downstairs == same column, next row
    # left == same row, previous column
    # right == same row, next column
    # if there's index error the answer is nobody
    """
    neighbour = ""
    for row in range(0, rows_cols):
        for col in range(0, rows_cols):
            if matrix[row][col] == person:
                if direction == "upstairs" and row > 0:
                    neighbour = matrix[row - 1][col]
                elif direction == "downstairs" and row < rows_cols - 1:
                    neighbour = matrix[row + 1][col]
                elif direction == "left" and col > 0:
                    neighbour = matrix[row][col - 1]
                elif direction == "right" and col < rows_cols - 1:
                    neighbour = matrix[row][col + 1]
                else:
                    neighbour = "nobody"

    return neighbour


if __name__ == '__main__':
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
    print(find_neighbour(cubeStr, "  Tom:    My upstairs neighbor is (?)"))
