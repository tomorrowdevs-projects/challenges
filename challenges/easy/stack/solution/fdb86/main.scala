import scala.collection.mutable.Stack

object Main {
  var mystack: Stack[Int] = Stack(1,2,3);
  def main(args: Array[String]): Unit = {

    println("Elements of mystack = " + mystack)

    // push
    println("\nElements of mystack after pushing 1 elem (5) = " + mystack.push(5))

    // pop
    println("\nPopped 1 elem = " + mystack.pop)
    println("\nElements of mystack after popped 1 elem (method LIFO) = " + mystack)
    
    // peek
    println("\nThe top element in mystack = " + mystack.top)

    // isEmpty
    println("\nMystack is empty? " + mystack.isEmpty)

    // size
    println("\nSize of mystack = " + mystack.size)

  }
}
