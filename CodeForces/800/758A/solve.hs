main = do
    content <- getContents
    let listOfNumbers = map (read::String->Int) . words . last $ lines content
    let maximumNumber = maximum listOfNumbers
    let listOfDifferences = [maximumNumber - x | x <- filter (/=maximumNumber) listOfNumbers]
    print $ sum listOfDifferences