import Data.List
main = do 
    content <- getContents
    let listOfLists = map(map(read::String->Int).words) $ tail . lines $ content
    let before = [head x | x <-listOfLists]
    let after = [last x | x <-listOfLists]
    let sorted = reverse $ sort before
    if before /= after then putStr "rated" else if before == sorted then putStr "maybe" else putStr "unrated"