;; Clojure solution for easy challenge: "Queue"

;; Queue Class
(ns Queue (:gen-class))

(defn -setQueue [] (def .queue []))

;; ENQUEUE method => Adds an item to the queue (FIFO)
(defn -enqueue [queue item] (def .queue (conj queue item)))

;; DEQUEUE method => Removes the first item from the queue (FIFO)
(defn -dequeue [queue] (def .queue (subvec queue 1)))

;; PEEK method => Returns the next item in the queue without removing it
(defn -peek [queue] (first queue))

;; ISEMPTY method => Returns a boolean indicating whether or not the queue is empty
(defn -isEmpty [queue] (empty? queue))

;; SIZE method => Returns the number of items in the queue
(defn -size [queue](count queue))


;; IMPLEMENTATION TEST
;; QUEUE initialization
(Queue/-setQueue)
(print "\nINITIAL QUEUE: ")
(println .queue)
;; ENQUEUE test
(println "\nENQUEUE (each time adds an item to the queue (FIFO)): ")
(-enqueue .queue 1)
(println .queue)
(-enqueue .queue 2)
(println .queue)
(-enqueue .queue 3)
(println .queue)
(-enqueue .queue 4)
(println .queue)
;; DEQUEUE test
(println "\nDEQUEUE (each time removes an item from the queue (FIFO)): ")
(-dequeue .queue)
(println .queue)
;; PEEK test
(print "\nPEEK (returns the next item in the queue without removing it): ")
(println (-peek .queue))
;; ISEMPTY test
(print "\nThe QUEUE is EMPTY ? ")
(println (-isEmpty .queue))
;; SIZE test
(print "\nNUMBER of ITEMS in the queue: ")
(println (-size .queue))
;; DEQUEUE test
(println "\nDEQUEUE (each time removes an item from the queue (FIFO)): ")
(-dequeue .queue)
(println .queue)
(-dequeue .queue)
(println .queue)
(-dequeue .queue)
(println .queue)
;; SIZE test
(print "\nNUMBER of ITEMS in the queue: ")
(println (-size .queue))
;; ISEMPTY test
(print "\nThe QUEUE is EMPTY ? ")
(println (-isEmpty .queue) "\n")