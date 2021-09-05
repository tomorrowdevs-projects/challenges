import Data.List
import Data.Char

uppercase :: String -> String
uppercase = map toUpper

replace :: String -> Char -> String -> String
replace xs c s = foldr go [] xs
    where go x acc = if x == c  then s ++ acc 
                                else [x] ++ acc 
                                
main = print (vaporcode_string)
    where
        input_string = " Hello Folks. This is Haskell! " -- try changing this
        string_uppercase = uppercase input_string
        string_nospace = replace string_uppercase ' ' ""
        string_onespaced = intersperse ' ' string_nospace
        vaporcode_string = intersperse ' ' string_onespaced  -- adding 2nd space
