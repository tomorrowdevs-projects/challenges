-- Haskell solution for challenge: "Vaporcode"

module Vaporcode where
import Data.Char

vaporcode :: String -> String
vaporcode str = (reverse . drop 2 . reverse)(map toUpper(concatMap(\x -> if x /= ' ' then [x] ++ "  " else "") str))

-- Resolution algorithm
--    Adding two spaces for each character of the string (other than the space itself)
--    Capitalization of the string
--    Deleting two spaces at the end of the string