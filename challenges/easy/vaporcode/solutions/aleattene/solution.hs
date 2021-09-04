-- Haskell solution for challenge: "Vaporcode"

module Vaporcode where
import Data.Char

vaporcode :: String -> String

-- Removing the last two spaces of the string
removeLastTwoSpaces = reverse . drop 2 . reverse

-- Adding two spaces for each character of the string (other than the space itself)
-- Capitalization of the string
-- Deleting two spaces at the end of the string
vaporcode str = removeLastTwoSpaces(map toUpper(concatMap(\x -> if x /= ' ' then [x] ++ "  " else "") str))