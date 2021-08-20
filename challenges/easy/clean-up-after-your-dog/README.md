# Clean up after your dog

You have stumbled across the divine pleasure that is owning a dog and a garden. Now time to pick up all the cr@p! 😄 <br />
Given a 2D array to represent your garden, you must find and collect all of the dog cr@p - represented by `@`.

You will also be given the number of bags you have access to (bags), and the capacity of a bag (cap). If there are no bags then you can't pick anything up, so you can ignore cap.<br />
You need to find out if you have enough capacity to collect all the cr@p and make your garden clean again.

If you do, return 'Clean',else return 'Cr@p'.

Watch out though - if your dog is out there ('D'), he gets very touchy about being watched. If he is there you need to return 'Dog!!'.

# Examples

**JavaScript**

```js
const garden1 = [
  ['_','_','_','_','_','_'],
  ['_','_','_','_','@','_'],
  ['@','_','_','_','_','_']
];

const garden2 = [
  ['_','_','_','_'],
  ['_','_','_','_'],
  ['@','_','_','D']
];

function cleanUp(garden, bags, cap) {
  // your code here
}

cleanUp(garden1, 2, 2) == 'Clean';
cleanUp(garden1, 1, 1) == 'Cr@p';
cleanUp(garden2, 2, 2) == 'Dog!!';
```

**Python**

```python
garden1 = [
  ['_','_','_','_','_','_'],
  ['_','_','_','_','@','_'],
  ['@','_','_','_','_','_']
]

garden2 = [
  ['_','_','_','_'],
  ['_','_','_','_'],
  ['@','_','_','D']
]

def cleanUp(garden, bags, cap):
  # your code here

cleanUp(garden1, 2, 2) == 'Clean'
cleanUp(garden1, 1, 1) == 'Cr@p'
cleanUp(garden2, 2, 2) == 'Dog!!'
```

# Test cases

```python
cleanUp([['_','_','_','_'], ['_','_','_','@'], ['_','_','@','_']], 2, 2) == 'Clean'
cleanUp([['_','_','_','_'], ['_','_','_','@'], ['_','_','@','_']], 1, 1) == 'Cr@p'
cleanUp([['_','_'], ['D','_'], ['_','_']], 2, 2) == 'Dog!!'
cleanUp([['_','_','_','_'], ['_','_','_','_'], ['_','_','_','_']], 2, 2) == 'Clean'
cleanUp([['@','@'], ['@','@'], ['@','@']], 3, 2) == 'Cr@p'
cleanUp([['_','_','_','_','D','_','_','_','_'], ['_','_','_','_','@','@','_','_','_'], ['_','_','_','_','_','_','D','_','_']], 9, 5) == 'Dog!!'
cleanUp([['_','_','_','_','_']], 6, 9) == 'Clean'
cleanUp([['_','_','D','_','_','_','_','_','D'], ['_','_','D','_','_','_','_','_','_'], ['_','_','_','_','_','@','_','_','_']] , 4, 4) == 'Dog!!'
cleanUp([['_','@','@'], ['_','@','@']]), 1, 2) == 'Cr@p'
cleanUp([['_','_','_','_','_','_','_','@'], ['_','_','_','@','D','_','_','_'], ['_','_','_','_','_','_','D','_'], ['_','_','_','_','D','_','_','_'], ['_','_','_','_','D','@','_','_']], 1, 6) == 'Dog!!'
cleanUp([['_','_','_','_','_','_','_','@','_'], ['_','_','_','_','_','_','_','@','_']], 4, 3) == 'Clean'
cleanUp([['_','_','_','_','_']], 6, 0) == 'Clean'
cleanUp([['_','@','@','_','_','@','_','_','_']], 4, 0) == 'Cr@p'
cleanUp([['D','_','_','_'], ['_','_','_','_'], ['_','_','_','_'], ['_','_','@','_'], ['_','_','_','_']], 7, 8) == 'Dog!!'
cleanUp([['_','@','_'], ['_','@','_']]), 0, 8) == 'Cr@p'
```