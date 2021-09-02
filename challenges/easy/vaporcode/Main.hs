import Data.Char
import Data.String
import Data.List (tails)

isUp :: Char -> Bool
isUp = (`elem` ['A'..'Z'])

isLow :: Char -> Bool  
isLow = (`elem` ['a'..'z'])

isWhite :: Char -> Bool
isWhite = (`elem` [' '])


-- convert a char to uppercase
toUp :: Char -> Char
toUp x = if isLow x then toEnum (fromEnum x - 32) else x

-- convert a string to uppercase using map and toUp
toUpStr :: String -> String
toUpStr str = map toUp str

-- split a string to single chars
mySplit :: String -> [String]
mySplit str = filter (\s -> length s == 1) $ map (take 1) (tails str)

--remove whitespace from a list
remove list = filter (\e -> e/=" ") list

-- return a new string using the buid function unwords, that separates the chars using whitespaces
myVapor = unwords . remove . mySplit . toUpStr