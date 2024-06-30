import Data.List
main = interact $ f . sort . map read . words
f x = show $ last x - head x