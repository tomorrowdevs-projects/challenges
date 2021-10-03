// use ArrayList instead of array to have different data types
class MyStack extends java.util.ArrayList{
  //
  public boolean isEmpty(){
    //return true if the size of the array is 0;
    return super.size() == 0;
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
      return "The stack is empty";
    }
  }

  public Object pop(){
    if(super.size() > 0){
      // get the last element and remove it
      Object obj = get(size() -1);
      remove(obj);
      return obj;
    }
    else{
      return "The stack is empty";
    }
  }

  public Object push(Object obj){
    // add new element to the object
    add(obj);
    return obj;
  }
}


public class Main{
  // new object
  MyStack stack = new MyStack();

  public static void main(String[] args){
    MyStack stack = new MyStack();

    // testing the stack
    stack.push("Test");
    stack.push(1);
    System.out.println(stack.isEmpty());
    stack.push(10);
    System.out.println(stack.size());
    System.out.println(stack.peek());
    stack.pop();
    System.out.println(stack.size());
    System.out.println(stack.peek());
    stack.pop();
    System.out.println(stack.peek());
    stack.pop();
    stack.pop();
    stack.pop();
    System.out.println(stack.isEmpty());
  }
}
