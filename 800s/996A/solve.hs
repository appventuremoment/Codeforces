main = interact $ show.f.read
f x = x `div` 100 + x `mod` 100 `div` 20 + x `mod` 100 `mod` 20 `div` 10 + x `mod` 100 `mod` 20 `mod` 10 `div` 5 + x `mod` 100 `mod` 20 `mod` 10 `mod` 5