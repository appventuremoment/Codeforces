main = do
    content <- getContents
    let cal = 0 : map (read::String->Int) (words (head $ lines content))
    let numbersList = map ((read::String->Int).(:[])) (last $ lines content)
    let answer = [cal !! x | x <- numbersList]
    print $ sum answer