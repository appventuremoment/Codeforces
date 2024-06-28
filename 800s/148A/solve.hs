main = interact $ show . f . lines
f x = do
    let factors = map read $ take 4 x
    let number = read $ last x
    let listOfDrags = [x | x <- [1..number], any (\factor -> x `mod` factor == 0) factors]
    length listOfDrags