main = do
    contents <- getContents
    let n = (read::String->Int) contents
    let numberOfPrimes = n `div` 2
    let listOf2s = if even n then  ["2" |x <- [1..numberOfPrimes]] else "3" : ["2" |x <- [1..numberOfPrimes - 1]]
    putStrLn $ show numberOfPrimes
    putStrLn $ unwords listOf2s