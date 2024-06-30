-- This is a comment
{- This is a multi-line comment
test test
test -}

-- CUSTOM MODULE
module TestModule (gcdDef, switchFunction) where
import Data.Char
import Data.List
import System.IO
test = [0, 5..100] :: [Integer]
showPrint = show "im so tired"
printPrint = print "im so tired"
putPrint = putStrLn "im so tired"
modFunc = print $ 1 `mod` (-3)

tempList = [2..20]
listConditional = print [(x, y) | x <- tempList, x <= 8, y <- [1, 2, 3]]
zipWithExample = zipWith (\x y -> 2 * x + y) [1, 2, 3, 4, 5] [-1, -1, -1, -1, -1]
takeWhileExample = takeWhile (<= 10) [2..20] ++ [1]
customFunction (a, b, z) 91 = print $ a + b + z
customFunction (a, b, z) _ = print $ a + b

-- funny math function thingy
factorial 0 = 1
factorial n = n * factorial(n - 1)
permutation n r = factorial n `div` factorial (n - r)
combination n r = permutation n r `div` factorial r

-- GUARDS GET HIM
whatAge ages
    | age <= 0 = putStrLn "Leave the unborn alone. What did you intend to do with it?"
    | age > 0 && age <= 7 = putStrLn "Too young"
    | age > 7 = putStrLn "can drive"
    | age > 12 = putStrLn "has wings can fly"
    | otherwise = putStrLn "If I speak I am in big trouble" -- impossible to reach
    where age = max 12 ages

-- Recursion
gcdDef 0 0 = 1
gcdDef x 0 = x
gcdDef x y = gcdDef y x `mod` y

functionListInput (x:y:xs) = print x

showcaseMap = map (\x -> (x + 3) * 2) [1..10]
showCaseMap = map ((*2).(+3)) [1..10]

customEven n = if n `mod` 2 == 0 && n > 2 ^ 10 then "Even Number" else "Unfair Number"

switchFunction n = case n of
    "kitty" -> "catty"
    "doggy" -> "woof."
    _ -> "what"

-- Enums
data Day = Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday
    deriving (Eq, Ord, Show, Enum, Bounded)

isWeekEnd Saturday Sunday = print True
isWeekEnd Sunday Saturday = print True

-- Eq and Ord just mean comparison (==, >, <, /=)
-- Show is quite literally ability to be pritned
-- Enum means ability to use succ/pred, which gives the element after/before the one in input as argument
-- Bounded means ability to use minBounded/maxBounded, which gives first/last element of enum respectively

data Customer = Customer {
    name :: String,
    balance :: Double 
    } deriving (Show, Eq)

getBalance (Customer _ bal) = putStrLn $ "You have " ++ show bal ++ " dollars left. Live cautiously."
testgetBalance = getBalance $ Customer {name = "person", balance = 20.05}
-- or Customer "person" 20.05

data ShirtSize = XS | S | M | L | XL | XXL | XXXL
instance Show ShirtSize where
    show XS = "Xtra Small"
    show S = "Small"
    show M = "Medium"
    show L = "Large"
    show XL = "Xtra Large"
    show XXL = "Xtra Xtra Large"

-- Custom comparators need to define the function names explicitely beforehand
class MyEq c where
    areEqual :: c -> c -> Bool
instance MyEq Customer where
    areEqual (Customer n1 _) (Customer n2 _) = n1 == n2

-- File IO
writetoFile = do
    fileName <- openFile "test.txt" WriteMode
    hPutStrLn fileName "Random Text"
    hPutStrLn fileName "Random Text"
    hPutStrLn fileName "Random Text"
    hClose fileName

readfromFile = do
    fileName <- openFile "test.txt" ReadMode
    contents <- hGetContents fileName
    putStr contents
    hClose fileName
    
fibSeq = [1,1] ++ [a + b | (a, b) <- zip fibSeq (tail fibSeq)]
fibNumber n = fibSeq !! (n - 1)

summation = [sum [1..n] | n <- [1..]]
sumN n = summation !! (n - 1)
-- or sumN n = sum [1..n]