import java.util.Arrays;


class Queue {
  private int capacity;
  private int arr[];
  private int front;
  private int rear;
  private int size;

  // constructor of the class with the capacity as parameter
  public Queue(int s) {
    arr = new int[s];  // empty array with given capacity
    capacity = s;
    size = 0;
    front = capacity - 1;  // first element which gets deleted
    rear = -1;  // last element which gets deleted
  }

  public boolean isEmpty() {
    if (size == 0) {
      return true;
    } else {
      return false;
    }
  }

  public boolean isFull() {
    return this.size == this.capacity;
  }

  // adds an element to the stack
  public void enqueue(int x) {
    if (isFull()) {
      System.out.println("no more space in the queue!");
    }
    else {
      // the newest element will go in the first available slot starting from left
      this.rear = capacity - size - 1;
      this.arr[rear] = x;
      this.size = size + 1;
    }
  }

  public void dequeue() {
    if (isEmpty()) {
      System.out.println("empty queue!");
    }
    else {
      // new empty array gets created, with same capacity
      this.size = size - 1;
      int[] arr = new int[capacity];
      // filling the new array (from the right) with all the previous elements except the front one
      int j = 0;  // will point to the previous array
      for (int i = 1; i < capacity; i++) {
        arr[i] = this.arr[j];
        j = j + 1;
      }
      this.arr = arr;  // substituting old array with new
      this.front = capacity - 1;
    }
  }

  public Integer peek() {  // Integer allows returning null
    if (!isEmpty()) {
      return this.arr[this.front];
    }
    return null;
  }

  public int size() {
    return this.size;
  }

  public void displayQueue() {
    System.out.println(Arrays.toString(this.arr));
  }
}


class Main {
  public static void main(String[] args) {
    // instance of new queue
    Queue queue = new Queue(3);
    queue.displayQueue();
    System.out.println("current size: " + queue.size());
    System.out.println("");
    
    // filling the queue with new elements
    queue.enqueue(10);
    queue.displayQueue();
    System.out.println("front element is " + queue.peek());
    System.out.println("current size: " + queue.size());
    System.out.println("");
    queue.enqueue(15);
    queue.displayQueue(); 
    System.out.println("front element is " + queue.peek());
    System.out.println("current size: " + queue.size());
    System.out.println("");
    queue.enqueue(20);
    queue.displayQueue();
    System.out.println("front element is " + queue.peek());
    System.out.println("current size: " + queue.size());
    // the following has no effect --> queue is full
    queue.enqueue(30);
    System.out.println("");

    // freeing space in queue by removing all elements
    queue.dequeue();
    queue.displayQueue();
    System.out.println("front element is " + queue.peek());
    System.out.println("current size: " + queue.size());
    System.out.println("");
    queue.dequeue();
    queue.displayQueue();
    System.out.println("front element is " + queue.peek());
    System.out.println("current size: " + queue.size());
    System.out.println("");
    queue.dequeue();
    queue.displayQueue();
    System.out.println("front element is " + queue.peek());
    System.out.println("current size: " + queue.size());
    queue.dequeue();  // no effect, already  empty
    System.out.println("");

    // refilling and freeing again
    queue.enqueue(100);
    queue.enqueue(200);
    queue.enqueue(300);
    queue.dequeue();
    queue.displayQueue();
    System.out.println("front element is " + queue.peek());
  }
}