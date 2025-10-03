sumaFila :: [Integer] -> Integer
sumaFila [] = 0
sumaFila (x:xs) = x + sumaFila xs

sumaTotal :: [[Integer]] -> Integer
sumaTotal [] = 0
sumaTotal (x:xs) = sumaFila x + sumaTotal xs

cantidadAparicionesFila :: Integer -> [Integer] -> Integer
cantidadAparicionesFila _ [] = 0
cantidadAparicionesFila e (x:xs)
    | x == e = 1 + cantidadAparicionesFila e xs
    | otherwise = cantidadAparicionesFila e xs

cantidadDeApariciones :: Integer -> [[Integer]] -> Integer
cantidadDeApariciones _ [] = 0
cantidadDeApariciones e (x:xs) = cantidadAparicionesFila e x + cantidadDeApariciones e xs

contarPalabrasFila :: String -> [String] -> Integer
contarPalabrasFila _ [] = 0
contarPalabrasFila s (x:xs)
    | x == s = 1 + contarPalabrasFila s xs
    | otherwise = contarPalabrasFila s xs

contarPalabras :: String -> [[String]] -> Integer
contarPalabras s [] = 0
contarPalabras s (x:xs) = contarPalabrasFila s x + contarPalabras s xs

cantidadAparicionesFila2 :: (Eq a) => a -> [a] -> Integer
cantidadAparicionesFila2 _ [] = 0
cantidadAparicionesFila2 e (x:xs)
    | x == e = 1 + cantidadAparicionesFila2 e xs
    | otherwise = cantidadAparicionesFila2 e xs

cantidadDeApariciones2 :: (Eq a) => a -> [[a]] -> Integer
cantidadDeApariciones2 _ [] = 0
cantidadDeApariciones2 e (x:xs) = cantidadAparicionesFila2 e x + cantidadDeApariciones2 e xs

multiplicarFila :: Integer -> [Integer] -> [Integer]
multiplicarFila _ [] = []
multiplicarFila e (x:xs) = (e*x) : multiplicarFila e xs

multiplicarPorEscalar :: Integer -> [[Integer]] -> [[Integer]]
multiplicarPorEscalar _ [] = []
multiplicarPorEscalar e (x:xs) = (multiplicarFila e x) : multiplicarPorEscalar e xs

aplanarListaStrings :: [String] -> String
aplanarListaStrings [s] = s
aplanarListaStrings (s:ss) = s ++ aplanarListaStrings ss

concatenarFilas :: [[String]] -> [String]
concatenarFilas [] = []
concatenarFilas (x:xs) = aplanarListaStrings x : concatenarFilas xs

iEsimoElemento :: Integer -> [a] -> a
iEsimoElemento 0 (x:_) = x
iEsimoElemento i (x:xs) = iEsimoElemento (i-1) xs

iEsimaFila :: Integer -> [[a]] -> [a]
-- iEsimaFila _ [] = []
-- iEsimaFila 0 (x:xs) = x
-- iEsimaFila i (x:xs) = iEsimaFila (i-1) xs
iEsimaFila i xs = iEsimoElemento i xs

iEsimaColumna :: Integer -> [[a]] -> [a]
iEsimaColumna _ [] = []
iEsimaColumna i (x:xs) = iEsimoElemento i x : iEsimaColumna i xs

matrizIdentidad :: Integer -> [[Integer]]
matrizIdentidad 0 = []
matrizIdentidad n =  matrizIdentidadAux n n

matrizIdentidadAux :: Integer -> Integer -> [[Integer]]
matrizIdentidadAux n 1 = [iEsimaFilaIdentidad n 1]
matrizIdentidadAux n m = matrizIdentidadAux n (m-1) ++ [iEsimaFilaIdentidad n m]

iEsimaFilaIdentidad :: Integer -> Integer -> [Integer]
iEsimaFilaIdentidad 0 _ = []
iEsimaFilaIdentidad n i
    | i == n = iEsimaFilaIdentidad (n-1) i ++ [1]
    | otherwise = iEsimaFilaIdentidad (n-1) i ++ [0]

cantidadParesColumna :: Integer -> [[Integer]] -> Integer
cantidadParesColumna i xs = cantidadParesLista (iEsimaColumna i xs)

cantidadParesLista :: [Integer] -> Integer
cantidadParesLista [] = 0
cantidadParesLista (x:xs)
    | mod x 2 == 0 = 1 + cantidadParesLista xs
    | otherwise = cantidadParesLista xs