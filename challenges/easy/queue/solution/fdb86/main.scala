import scala.collection.mutable._

object Main {
  var myqueue = Queue(1, 2, 3, 4, 5)
  def main(args: Array[String]): Unit = {
    println("Queue elements: " + myqueue)

    // enqueue
    myqueue.enqueue(8)
    println("\nQueue elements after enqueue: " + myqueue)

    // dequeue
    var dequeued = myqueue.dequeue
    println("\nElement dequeued: " + dequeued)
    println("\nQueue elements after dequeue (method FIFO): " + myqueue)

    // isEmpty
    println("\nMyqueue is empty? " + myqueue.isEmpty)

    // size
    println("\nSize of myqueue = " + myqueue.size)

    // peek
    println("\nFirst element: " + myqueue.front)
  }
}
