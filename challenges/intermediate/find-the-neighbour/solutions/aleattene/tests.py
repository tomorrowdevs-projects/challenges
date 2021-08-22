
""" To start the tests, type from CLI: python tests.py """

import unittest
from solution import find_neighbour


class TestSolution(unittest.TestCase):

    def test_tom_neighbours(self):
        cube_str = """
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
        self.assertEqual(find_neighbour(cube_str, "Tom: My left neighbor is (?)"), "nobody")
        self.assertEqual(find_neighbour(cube_str, "Tom: My upstairs neighbor is (?)"), "nobody")
        self.assertEqual(find_neighbour(cube_str, "Tom: My right neighbor is (?)"), "Jerry")
        self.assertEqual(find_neighbour(cube_str, "Tom: My downstairs neighbor is (?)"), "Mike")

    def test_jerry_neighbours(self):
        cube_str = """
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
        self.assertEqual(find_neighbour(cube_str, "Jerry: My left neighbor is (?)"), "Tom")
        self.assertEqual(find_neighbour(cube_str, "Jerry: My upstairs neighbor is (?)"), "nobody")
        self.assertEqual(find_neighbour(cube_str, "Jerry: My right neighbor is (?)"), "John")
        self.assertEqual(find_neighbour(cube_str, "Jerry: My downstairs neighbor is (?)"), "Peter")

    def test_john_neighbours(self):
        cube_str = """
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
        self.assertEqual(find_neighbour(cube_str, "John: My left neighbor is (?)"), "Jerry")
        self.assertEqual(find_neighbour(cube_str, "John: My upstairs neighbor is (?)"), "nobody")
        self.assertEqual(find_neighbour(cube_str, "John: My right neighbor is (?)"), "nobody")
        self.assertEqual(find_neighbour(cube_str, "John: My downstairs neighbor is (?)"), "Alice")

    def test_mike_neighbours(self):
        cube_str = """
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
        self.assertEqual(find_neighbour(cube_str, "Mike: My left neighbor is (?)"), "nobody")
        self.assertEqual(find_neighbour(cube_str, "Mike: My upstairs neighbor is (?)"), "Tom")
        self.assertEqual(find_neighbour(cube_str, "Mike: My right neighbor is (?)"), "Peter")
        self.assertEqual(find_neighbour(cube_str, "Mike: My downstairs neighbor is (?)"), "Bob")

    def test_peter_neighbours(self):
        cube_str = """
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
        self.assertEqual(find_neighbour(cube_str, "Peter: My left neighbor is (?)"), "Mike")
        self.assertEqual(find_neighbour(cube_str, "Peter: My upstairs neighbor is (?)"), "Jerry")
        self.assertEqual(find_neighbour(cube_str, "Peter: My right neighbor is (?)"), "Alice")
        self.assertEqual(find_neighbour(cube_str, "Peter: My downstairs neighbor is (?)"), "Bill")

    def test_alice_neighbours(self):
        cube_str = """
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
        self.assertEqual(find_neighbour(cube_str, "Alice: My left neighbor is (?)"), "Peter")
        self.assertEqual(find_neighbour(cube_str, "Alice: My upstairs neighbor is (?)"), "John")
        self.assertEqual(find_neighbour(cube_str, "Alice: My right neighbor is (?)"), "nobody")
        self.assertEqual(find_neighbour(cube_str, "Alice: My downstairs neighbor is (?)"), "Wang")

    def test_bob_neighbours(self):
        cube_str = """
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
        self.assertEqual(find_neighbour(cube_str, "Bob: My left neighbor is (?)"), "nobody")
        self.assertEqual(find_neighbour(cube_str, "Bob: My upstairs neighbor is (?)"), "Mike")
        self.assertEqual(find_neighbour(cube_str, "Bob: My right neighbor is (?)"), "Bill")
        self.assertEqual(find_neighbour(cube_str, "Bob: My downstairs neighbor is (?)"), "nobody")

    def test_bill_neighbours(self):
        cube_str = """
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
        self.assertEqual(find_neighbour(cube_str, "Bill: My left neighbor is (?)"), "Bob")
        self.assertEqual(find_neighbour(cube_str, "Bill: My upstairs neighbor is (?)"), "Peter")
        self.assertEqual(find_neighbour(cube_str, "Bill: My right neighbor is (?)"), "Wang")
        self.assertEqual(find_neighbour(cube_str, "Bill: My downstairs neighbor is (?)"), "nobody")

    def test_wang_neighbours(self):
        cube_str = """
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
        self.assertEqual(find_neighbour(cube_str, "Wang: My left neighbor is (?)"), "Bill")
        self.assertEqual(find_neighbour(cube_str, "Wang: My upstairs neighbor is (?)"), "Alice")
        self.assertEqual(find_neighbour(cube_str, "Wang: My right neighbor is (?)"), "nobody")
        self.assertEqual(find_neighbour(cube_str, "Wang: My downstairs neighbor is (?)"), "nobody")


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()
