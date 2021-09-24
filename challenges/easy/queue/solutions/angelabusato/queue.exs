defmodule Queue do
    def enqueue(queue, elem) do
        [elem | queue]
    end
    def dequeue(queue) do
        queue |> Enum.reverse() |> tl() |> Enum.reverse()
    end
    def peek(queue) do
        List.last(queue)
    end
    def isEmpty(queue) do
        Enum.empty?(queue)
    end
    def size(queue) do 
        Enum.count(queue)
    end
end

queue = []

IO.inspect(queue, label: "Queue")
queue = Queue.enqueue(queue, 1)
IO.inspect(queue, label: "Enqueued 1")
queue = Queue.enqueue(queue, 2)
IO.inspect(queue, label: "Enqueued 2")
queue = Queue.enqueue(queue, 3)
IO.inspect(queue, label: "Enqueued 3")
queue = Queue.dequeue(queue)
IO.inspect(queue, label: "Dequeued")
firstEl = Queue.peek(queue)
IO.inspect(firstEl, label: "Queue first Element")
empty = Queue.isEmpty(queue)
IO.inspect(empty, label: "Queue is empty?")
size = Queue.size(queue)
IO.inspect(size, label: "Queue size")