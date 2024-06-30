main = interact $ f . map read . words
f x = show (min red blue) ++ " " ++ show ((max red blue - min red blue) `div` 2) where 
    red = head x
    blue = last x
