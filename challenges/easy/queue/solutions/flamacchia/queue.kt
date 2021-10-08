/* 
add a list as parameter in constructor
*/

class Queue(

    var list: MutableList<Any>

) {

    // adds an item to the queue
    fun enqueue(item : Any) {
        list.add(item)
    }

    // returns the next item in the queue
    fun dequeue() {
        list.removeAt(0)
    }

    // returns the next item in the queue
    fun peek() : Any {
        return list[0]
    }

    //tests to see whether the queue is empty
    fun isEmpty() : Boolean {

        return list.isEmpty()
    }

    // returns the number of items in the queue
    fun size() : Int {

        return list.size
    }

        
}


// example
var frutta = Queue (mutableListOf("Banana", "Mela", 1))

// main function
fun main(){
    println(frutta.list)
    frutta.enqueue("Mango")
    println(frutta.list)
    frutta.dequeue()
    println(frutta.list)
    println(frutta.peek())
    println(frutta.isEmpty())
    println(frutta.size())
}    