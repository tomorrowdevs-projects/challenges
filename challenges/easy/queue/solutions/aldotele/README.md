## Queue implemented in Java

A **Queue** is a linear data structure where elements can only be inserted from one side called
**rear** and deleted only from the opposite side called **front**, which means
the Queue follows the FIFO principle (*First-in First-out*), as opposed to the **Stack**, which follows
a LIFO principle (*Last-in First-out*).

We can easily think of a queue as a line of people in real-life. The first person to come will also be
the first person to be served, while the last person approaching the line will have to wait for all other
people to be served.

One example of application of queue data structures might be serving requests on a single shared resource, like a printer or CPU task scheduling.

[*Source*](https://www.studytonight.com/data-structures/queue-data-structure)

### methods
The Queue has the following methods:

  - `enqueue(item)` - adds an item to the queue
  - `dequeue()` - removes an item from the queue (FIFO)
  - `peek()` - returns the next item in the queue without removing it
  - `isEmpty()` - tests to see whether the queue is empty
  - `size()` - returns the number of items in the queue

## Code execution
From CLI, type:\
`javac Main.java`\
`java Main`
