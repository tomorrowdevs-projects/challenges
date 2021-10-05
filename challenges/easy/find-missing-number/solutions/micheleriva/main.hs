solution :: [Int] -> Int
solution xs = (-) (sum [(foldr1 min xs)..(foldr1 max xs)]) (sum xs)