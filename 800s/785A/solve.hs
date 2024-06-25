p "Tetrahedron" = 4; p "Cube" = 6; p "Octahedron" = 8; p "Dodecahedron" = 12; p "Icosahedron" = 20; main = interact $ show . sum . map p . tail . lines
-- main = interact $ show . sum . map p . tail . lines
