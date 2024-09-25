import Data.Char
main = do
    contents <- getContents
    let listOfYes = tail . lines $ contents
    let boolist = [if map toUpper testcase == "YES" then "YES" else "NO" | testcase <- listOfYes]
    putStrLn $ unlines boolist