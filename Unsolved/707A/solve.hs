main = do
    content <-getContents
    let listOfPixels = words . unwords . tail . lines $ content
    if "C" `elem` listOfPixels || "M" `elem` listOfPixels || "Y" `elem` listOfPixels then putStr "#Color" else putStr "#Black&White"