main = do
    contents <- getContents
    let n = read . head $ words contents
    let k = read . last $ words contents
    let ret = length [x | x <- [1..n], sum [1..x] * 5 <= (240 - k)]
    print ret