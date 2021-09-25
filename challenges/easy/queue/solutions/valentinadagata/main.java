// use ArrayList instead of array to have different data types
class MyQueue extends java.util.ArrayList{
  //
  public boolean isEmpty(){
    //return true if the size of the array is 0;
    if(super.size() == 0){
      return true;
    }
    else{
      return false;
    }
  }

  public int size(){
    // return the size of the array
    return super.size();
  }

  public Object peek(){
    // return the last element
    if(super.size() > 0){
      return get(size() -1);
    }
    else{
      return "The queue is empty";
    }
  }

  public Object dequeue(){
    if(super.size() > 0){
      // get the last element and remove it
      Object obj = get(size() -1);
      remove(obj);
      return obj;
    }
    else{
      return "The queue is empty";
    }
  }

  public Object enqueue(Object obj){
    // add new element to the object
    add(0, obj);
    return obj;
  }
}


public class Main{
  // new object
  MyQueue queue = new MyQueue();

  public static void main(String[] args){
    MyQueue queue = new MyQueue();

    // testing the queue
    queue.enqueue("Test");
    queue.enqueue(1);
    System.out.println(queue.peek());
    System.out.println(queue.isEmpty());
    queue.enqueue(100);
    queue.enqueue("Hello");
    queue.enqueue("World");
    System.out.println(queue.size());
    System.out.println(queue.peek());
    queue.dequeue();
    System.out.println(queue.peek());
    queue.dequeue();
    System.out.println(queue.peek());
    queue.dequeue();
    System.out.println(queue.peek());
    queue.dequeue();
    System.out.println(queue.peek());
    System.out.println(queue.size());
    System.out.println(queue.isEmpty());
  }
}