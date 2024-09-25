main = do
    number <- getContents
    let len = length number - 2
    let firstDigit = (read::String->Int) $ head $ map (:[]) number
    print $ (firstDigit + 1) * 10 ^ len - read number