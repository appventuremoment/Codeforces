p 1 = "1/1"
p 2 = "5/6"
p 3 = "2/3"
p 4 = "1/2"
p 5 = "1/3"
p 6 = "1/6"

main = interact $ p . maximum . map read . words