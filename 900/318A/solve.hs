main = do
    contents <- getContents
    let n = (read::String->Int) $ head $ words contents
    let k =  (read::String->Int) $ last $ words contents
    let halfway = n `mod` 2 + n `div` 2
    if k > halfway then print $ (k - halfway) * 2 else print $ k * 2 - 1