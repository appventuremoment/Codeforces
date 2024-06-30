main = do
    content <- getContents  
    let scoreList = map (read::String->Int) . words $ lines content !! 1
    let boolean = [x | x <- [1..length scoreList - 1], let round = take (x + 1) scoreList, let mostrecent = last round, (minimum round == mostrecent || maximum round == mostrecent) && length (filter (==mostrecent) round) == 1]
    print $ length boolean