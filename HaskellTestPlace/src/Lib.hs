module Lib
    ( someFunc
    ) where

-- This is a comment
{- This is a multi-line comment
test test
test -}
import Data.Char
import Data.List
test = [0, 5..100] :: [Integer]
someFunc :: IO ()
someFunc = print test
modFunc = print $ 1 `mod` (-3)


main = interact $ show.f.read
f = length . nub . filter isLetter