main = do
    contents <- getContents
    let listOfNumbers = tail . lines $ contents
    let listOfA = [(read::String->Int) . head $ words x | x <- listOfNumbers]
    let listOfB = [(read::String->Int). last $ words x | x <- listOfNumbers]
    let answerList = [show ((diff `div` 10) + min 1 (diff `mod` 10)) | (a, b) <- zip listOfA listOfB, let diff = abs $ a - b]
    putStrLn $ unlines answerList