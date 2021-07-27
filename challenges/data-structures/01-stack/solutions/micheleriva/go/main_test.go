package main

import "testing"

func TestStackMethods(t *testing.T) {
	stack := &Stack{}
	stack.Push(1)
	stack.Push(2)
	stack.Push(3)

	if stack.Size() != 3 {
		t.Error("Stack size should be 3")
	}

	stack.Push(4)

	if stack.Size() != 4 {
		t.Error("Stack size should be 4")
	}

	if stack.IsEmpty() {
		t.Error("Stack isn't empty")
	}

	if stack.Peek() != 4 {
		t.Error("Stack peek should be 4")
	}

	pop1 := stack.Pop()

	if stack.Size() != 3 {
		t.Error("Stack size should be 3")
	}

	if pop1 != 4 {
		t.Error("Stack pop should be 4")
	}

	pop2 := stack.Pop()

	if pop2 != 3 {
		t.Error("Stack pop should be 3")
	}

	if stack.Size() != 2 {
		t.Error("Stack size should be 2")
	}
}
