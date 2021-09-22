;; Clojure solution for easy challenge: "Queue"

;; Class Queue
(ns Queue (:gen-class :init init))

(defn init [queue] (def .queue queue))

;; enqueue method
(defn enqueue [queue item] (def .queue (conj queue item)))

;; dequeue method
(defn dequeue [queue] (def .queue (pop queue)))

;; peek method => is a built-in clojure function

;; size method
(defn size [queue](count queue))

;; isEmpty function
(defn isEmpty [queue] (empty? queue))


;; IMPLEMENTATION TEST
(def initialQueue [1 2 3])
;; queue initialization
(Queue/init initialQueue)
(print "\nINITIAL QUEUE: ")
(println .queue)
;; enqueue test
(println "\nENQUEUE (add item(s) to queue): ")
(enqueue .queue 4)
(println .queue)
(enqueue .queue 5)
(println .queue)
;; dequeue test
(println "\nDEQUEUE (remove item(s) from queue): ")
(dequeue .queue)
(println .queue)
;; peek test
(print "\nPEEK (return last item of queue): ")
(println (peek .queue))
;; isEmpty test
(print "\nThe QUEUE is EMPTY ? ")
(println (isEmpty .queue))
;; size test
(print "\nSIZE QUEUE: ")
(println (size .queue))
;; dequeue test
(println "\nDEQUEUE (remove item(s) from queue): ")
(dequeue .queue)
(println .queue)
(dequeue .queue)
(println .queue)
(dequeue .queue)
(println .queue)
(dequeue .queue)
(println .queue)
;; size test
(print "\nSIZE QUEUE: ")
(println (size .queue))
;; isEmpty test
(print "\nThe QUEUE is EMPTY ? ")
(println (isEmpty .queue) "\n")