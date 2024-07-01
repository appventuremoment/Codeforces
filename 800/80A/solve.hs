import Data.List
isPrime k = (k > 1) && null [ x | x <- [2..k - 1], k `mod` x == 0]
listOfPrimes n = [x | x <- [1..n], isPrime x]
main = do
    content <- getContents
    let [n, m] = map (read :: String -> Int) (words content)
    let primesList = listOfPrimes 50
    case elemIndex n primesList of
        Just idx -> if idx + 1 < length primesList && primesList !! (idx + 1) == m
                    then putStrLn "YES"
                    else putStrLn "NO"
        Nothing -> putStrLn "NO"