main = do
    contents <- getContents
    let listofnumbers = tail . lines $ contents
    let boolist = [if sum (map (read . (:[])) (take 3 contents)) == sum (map (read . (:[])) (drop 3 contents)) then "YES" else "NO" | contents <- listofnumbers]
    putStrLn $ unlines boolist