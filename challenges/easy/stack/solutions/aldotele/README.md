## Stack implemented in Java

A **Stack** is a linear data structure where elements are stacked on top of each other and 
only the top element can be accessed, which means the Stack follows a LIFO principle (*Last-in First-out*),
as opposed to the **Queue**, which follows a FIFO principle (*First-in-First-out*).

We can easily think of a stack as a line of plates: you cannot take the plate at the bottom
of the pile without removing, one by one, all the plates above.

Stack data structures are used when the order of actions matters. For example, when *reversing*
strings we would `push` each character onto the stack and then `pop` each character off.\
Also, programming languages use a stack to execute code: when a function is called it gets added to
to the *call-stack* and then removed once completed.

### methods
The Stack has the following methods:

- `push(item)` - Add an item to the top of the stack.
- `pop()` - Remove the top item from the stack.
- `peek()` - Returns a copy of the top item in the stack.
- `isEmpty()` - Return a boolean indicating whether or not the stack is empty.
- `size()` - Return the number of items in the stack.

## Code execution
From CLI, type:\
`javac Main.java`\
`java Main`