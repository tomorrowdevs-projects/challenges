;; Clojure solution for easy challenge: "Stack"

;; STACK Class
(ns Stack (:gen-class ))

(defn setStack [] (def .stack ()))

;; PUSH method =>  Adds an item to the top of the stack (LIFO)
(defn push [stack item] (def .stack (conj stack item)))

;; POP method => Removes the top item from the stack (LIFO) => Built-in Clojure function

;; PEEK method => Returns a copy of the top item in the stack => Built-in Clojure function

;; ISEMPTY method => Returns a boolean indicating whether or not the stack is empty
(defn isEmpty [stack] (empty? stack))

;; SIZE method => Returns the number of items in the stack
(defn size [stack](count stack))


;; IMPLEMENTATION TEST
(Stack/setStack)
(print "\nINITIAL STACK: ")
(println .stack)
;; PUSH test
(println "\nPUSH (each time adds an item to the top of the stack (LIFO)): ")
(push .stack 1)
(println .stack)
(push .stack 2)
(println .stack)
(push .stack 3)
(println .stack)
(push .stack 4)
(println .stack)
;; POP test
(println "\nPOP (each time removes the top item from the stack (LIFO)): ")
(def .stack (pop .stack))
(println .stack)
(def .stack (pop .stack))
(println .stack)
;; PEEK test
(print "\nPEEK (returns a copy of the top item in the stack): ")
(println (peek .stack))
;; ISEMPTY test
(print "\nThe STACK is EMPTY ? ")
(println (isEmpty .stack))
;; SIZE test
(print "\nNUMBER of ITEMS in the stack: ")
(println (size .stack))
;; POP test
(println "\nPOP (each time removes the top item from the stack (LIFO)): ")
(def .stack (pop .stack))
(println .stack)
(def .stack (pop .stack))
(println .stack)
;; SIZE test
(print "\nNUMBER of ITEMS in the stack: ")
(println (size .stack))
;; ISEMPTY test
(print "\nThe STACK is EMPTY ? ")
(println (isEmpty .stack) "\n")