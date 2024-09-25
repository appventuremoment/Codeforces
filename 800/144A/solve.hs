-- It just does not work.

-- import Data.List
-- import Data.Maybe
-- main = do
--     contents <- getContents
--     let listOfNumbers = map (read::String->Int) $ words . last $ lines contents
--     let maxIndex = fromJust $ maximum listOfNumbers `elemIndex` listOfNumbers
--     let minIndex = fromJust $ minimum listOfNumbers `elemIndex` listOfNumbers
--     if  maxIndex < minIndex  then print $ maxIndex + length listOfNumbers - minIndex - 1 else print $ maxIndex + length listOfNumbers - minIndex - 2

{-
import Data.List (elemIndices)

-- Function to find the index of the last occurrence of an element
lastIndexOf :: Eq a => a -> [a] -> Maybe Int
lastIndexOf x xs = case elemIndices x xs of
    [] -> Nothing         -- If the element is not found, return Nothing
    indices -> Just (last indices)  -- Otherwise, return the last index

main = do
    let list = [1, 2, 3, 2, 4, 2, 5]
    let element = 2
    print $ lastIndexOf element list

-}   