import Data.List
import Data.Char

remove_spaces :: String -> String
remove_spaces sentence = foldr go [] sentence
    where go x acc = if x == ' '  then "" ++ acc 
                                else [x] ++ acc 
                                
uppercase :: String -> String
uppercase = map toUpper

space :: String -> String
space string_nospace = intersperse ' ' string_nospace

double_space = space . space

vaporcode s = vaporwave
    where
        vaporwave = double_space(uppercase(remove_spaces(s)))

main = print(vaporcode "  Hello   World! This is haskell  !  ")