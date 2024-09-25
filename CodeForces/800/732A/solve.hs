main = interact $ f . map read . words
f x = show $ head [n | n <- [1..], cost * n `mod` 10 `elem` [k, 0]] where
    cost = head x
    k = last x