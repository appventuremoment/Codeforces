module Lib
    ( someFunc
    ) where

-- This is a comment
{- This is a multi-line comment
test test
test -}

test = [0, 5..100] :: [Integer]
someFunc :: IO ()
someFunc = print test
modFunc = print $ 1 `mod` (-3)
main = interact $ show . sum . head . lines
