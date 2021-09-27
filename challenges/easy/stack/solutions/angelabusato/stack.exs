defmodule Stack do
    def push(new, list) do
        [new | list]
    end
    def pop(list, index) do
        List.delete_at(list, index)
    end
    def peek(list) do
        List.first(list)
    end
    def isEmpty(list) do
        Enum.empty?(list)
    end
    def size(list) do 
        Enum.count(list)
    end
end

list = []

IO.inspect(list, label: "List")
list = Stack.push(1, list)
IO.inspect(list, label: "Pushed 1")
list = Stack.push(2, list)
IO.inspect(list, label: "Pushed 2")
list = Stack.push(3, list)
IO.inspect(list, label: "Pushed 3")
list = Stack.pop(list, 0)
IO.inspect(list, label: "Pop first element")
firstEl = Stack.peek(list)
IO.inspect(firstEl, label: "Stack top element")
empty = Stack.isEmpty(list)
IO.inspect(empty, label: "Stack is empty?")
size = Stack.size(list)
IO.inspect(size, label: "Stack size")