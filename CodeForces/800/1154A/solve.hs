import Data.List
main = do 
    contents <- getContents
    let numberList = sort $ map (read::String->Int) (words contents)
    let maxi = last numberList
    let a = maxi - head numberList 
    let b = maxi - numberList !! 1
    let c = maxi - numberList !! 2
    putStr $ show a ++ " " ++ show b ++ " " ++ show c