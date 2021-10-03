# When to use a stack

## Some examples

  - Stacks are particularly useful when the computation has to go back in reverse order.
  - The back button in a browser saves all the URLs you have visited previously in a stack. Each time you visit a new page, it is added on top of the stack. When you press the back button, the current URL is removed from the stack, and the previous URL is accessed.
  - Every time a function is called in a program, all the function’s arguments and local variables are stored by being pushed onto a stack. When the function exits, all that memory can be reclaimed by simply popping the stack back to where it was before the function call.
