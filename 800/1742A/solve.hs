import Data.List
main = do
    contents <- getContents
    let listofnumbers = tail . lines $ contents
    let boolist = [if last testcase == head testcase + testcase !! 1 then "YES" else "NO" | testcases <- listofnumbers, let testcase = sort $ map (read::String->Int) (words testcases)]
    putStrLn $ unlines boolist