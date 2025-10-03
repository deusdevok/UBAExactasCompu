sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs)
    | x == ' ' && y == ' ' = sacarBlancosRepetidos (y:xs)
    | otherwise = x : sacarBlancosRepetidos (y:xs)

contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras [x] 
    | x == ' ' = 0
    | otherwise = 1
contarPalabras (x:y:xs)
    | x /= ' ' && y == ' ' = 1 + contarPalabras xs
    | otherwise = contarPalabras (y:xs)

-- contarPalabras xs = length (palabras xs)

palabras :: [Char] -> [[Char]]
palabras [] = []
palabras (x:xs)
    | x == ' ' = palabras xs
    | otherwise = primeraPalabra (x:xs) : palabras (sacarPrimeraPalabra (x:xs))

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) 
    | x == ' ' = []
    | otherwise = x : primeraPalabra xs

sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra [] = []
sacarPrimeraPalabra (x:xs)
    | x == ' ' = xs
    | otherwise = sacarPrimeraPalabra xs

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga xs = masLarga (palabras xs)

masLarga :: [[Char]] -> [Char]
masLarga [x] = x
masLarga (x:y:xs) 
    | length x >= length y = masLarga (x:xs)
    | otherwise = masLarga (y:xs)

aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs

aplanar' :: Num a=> [[a]] -> [a]
aplanar'  = foldr (++) [3]
