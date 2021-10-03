module Likes where

import Text.Printf

likes :: [String] -> String
likes []       = "no one likes this"
likes [x]      = printf "%s likes this" x
likes [x,y]    = printf "%s and %s like this" x y
likes [x,y,z]  = printf "%s, %s and %s like this" x y z
likes (x:y:xs) = printf "%s, %s and %d others like this" x y (length xs)