main = do
    content <- getContents
    let n = (read::String->Int) content
    let listOfSums = [x * (x + 1) `div` 2 | x <- [1..n]]
    let listOfSumOfSums = [sum $ take x listOfSums | x <-[1..n], sum(take x listOfSums) <= n]
    putStrLn $ show $ length listOfSumOfSums