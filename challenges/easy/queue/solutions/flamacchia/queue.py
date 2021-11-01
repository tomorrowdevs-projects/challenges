""" 
add a list as parameter in constructor
"""

class Queue:

    # initialize list
    def __init__(self, list):
        self.list = list

    # adds an item to the queue
    def enqueue(self, new_item):

        self.list.append(new_item)

    # remove first item from the queue (FIFO) and not return it
    def dequeue(self):

        del self.list[0]

    # returns the next item in the queue
    def peek(self):

        return self.list[0]

    # tests to see whether the queue is empty
    def isEmpty(self):
        """ an Empty list is False in Python """

        return not bool(self.list)

    # returns the number of items in the queue
    def size(self):

        return len(self.list)



# example
frutta = Queue(["banana", "mela", "mango"])
print(frutta.list)
print(frutta.peek())
