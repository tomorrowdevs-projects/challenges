# Find the neighbour

Question: Do you know the names of neighbors? Look at the picture and answer the questions.

```
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
```

Write a function that returns the name of a given neighbour.

# Examples

**Python**

```python
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

def find_neighbour(cube, query):
    # your code here

# Test cases

find_neighbour(cubeStr, "Peter: My left neighbor is (?)") == "Tom"
find_neighbour(cubeStr, "Bob: My upstairs neighbor is (?)") == "Mike"
find_neighbour(cubeStr, "Tom: My right neighbor is (?)") == "Jerry"
find_neighbour(cubeStr, "Jerry: My downstairs neighbor is (?)") == "Peter"

# When there is no neighbour, return "nobody"

find_neighbour(cubeStr, "Wang: My right neighbor is (?)") == "nobody"
find_neighbour(cubeStr, "Wang: My downstairs neighbor is (?)") == "nobody"
find_neighbour(cubeStr, "Tom: My upstairs neighbor is (?)") == "nobody"
```

**JavaScript**

```js
const cubeStr = `
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
`;

function find_neighbour(cube, query) {
  // your code here
}

// Test cases

find_neighbour(cubeStr, "Peter: My left neighbor is (?)") === "Tom"
find_neighbour(cubeStr, "Bob: My upstairs neighbor is (?)") === "Mike"
find_neighbour(cubeStr, "Tom: My right neighbor is (?)") === "Jerry"
find_neighbour(cubeStr, "Jerry: My downstairs neighbor is (?)") === "Peter"

// When there is no neighbour, return "nobody"

find_neighbour(cubeStr, "Wang: My right neighbor is (?)") === "nobody"
find_neighbour(cubeStr, "Wang: My downstairs neighbor is (?)") === "nobody"
find_neighbour(cubeStr, "Tom: My upstairs neighbor is (?)") === "nobody"
```