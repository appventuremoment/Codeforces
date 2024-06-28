import Data.List (sort)
main = do
    input <- getContents
    let temp = lines input
    let firstpart = concat $ take 2 temp
    let secondpart = last temp
    if sort firstpart == sort secondpart then putStrLn "YES" else putStrLn "NO"