main = do
    contents <- getContents
    let listofnumbers = tail . lines $ contents
    let boolist = [(show . length) factors ++ "\n" ++ (unwords . map show) factors | n <- listofnumbers, let factors = [read n `div` (10 ^ (p - 1)) `mod` 10 * (10 ^ (p - 1)) | p <- [1..length n], read n `div` (10 ^ (p - 1)) `mod` 10 /= 0]]
    putStrLn $ unlines boolist