import java.util.Arrays;


class Stack {
  public int capacity;
  private int arr[];
  private int top;

  // constructor of the class with the capacity as parameter
  public Stack(int s) {
    arr = new int[s];  // empty array of a specific size
    capacity = s;
    top = -1;
  }

  public boolean isEmpty() {
    // following means a top element does not exist --> empty array
    return top == -1;
  }

  public boolean isFull() {
    // following means the top element reached the limit
    return top == capacity - 1;
  }

  // adds an element to the stack
  public void push(int x) {
    if (isFull()) {
      System.out.println("no more space in the stack!");
    }
    else {
      top = top + 1;
      // placing the number in the next available slot
      this.arr[top] = x;
    }
  }

  public void pop() {
    if (isEmpty()) {
      System.out.println("stack is already empty!");
    }
    else {
      // creating new array which excludes last element
      int[] arr = Arrays.copyOf(this.arr, this.arr.length - 1);
      // the top element is now at a lower index
      top = top - 1;
    }
  }

  public int size() {
    // currents size is the index of the top element + 1
    return top + 1;
  }

  public Integer peek() {  // Integer allows returning null
    if (!isEmpty()) {
      return this.arr[top];
    }
    return null;
  }

  public void displayStack() {    
    for (int i = 0; i <= top; i++) {
      System.out.print(this.arr[i] + ", ");
    }
    System.out.println("");
  }
}


class Main {
  public static void main(String[] args) {
    // initializing an empty stack with 3 available slots
    Stack stack = new Stack(3);
    stack.displayStack();  // nothing shown, empty array
    System.out.println(stack.capacity + " available spots");
    System.out.println("current size: " + stack.size());
    System.out.println("top element is " + stack.peek());
    // filling the slots
    stack.push(5);
    stack.displayStack();
    stack.push(6);
    stack.displayStack();
    stack.push(7);
    stack.displayStack();
    // getting current size
    System.out.println("current size: " + stack.size());
    // the following has no effect: already full
    stack.push(8);
    // removing items one by one
    stack.pop();
    stack.displayStack();
    stack.pop();
    stack.displayStack();
    stack.pop();
    stack.displayStack();
    // the following has no effect: already empty
    stack.pop();
    System.out.println("top element is " + stack.peek());
    // re-filling slots
    stack.push(10);
    stack.displayStack();
    System.out.println("top element is " + stack.peek());
    stack.push(20);
    stack.displayStack();
    System.out.println("top element is " + stack.peek());
    stack.push(30);
    stack.displayStack();
    System.out.println("top element is " + stack.peek());
  }
}