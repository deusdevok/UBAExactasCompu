sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

productoria :: [Integer] -> Integer
productoria [] = 0
productoria [a] = a
productoria (x:xs) = x * productoria xs

maximo :: (Ord t) => [t] -> t
maximo [a] = a
maximo (x:y:xs) | x > y = maximo (x:xs)
                | otherwise = maximo (y:xs)

maximo2 :: (Ord t) => [t] -> t
maximo2 [a] = a  
maximo2 (x:xs) | x > maximo2 xs = x
               | otherwise = maximo2 xs

maximo3 :: (Ord t) => [t] -> t
maximo3 [a] = a  
maximo3 (x:xs) = max x (maximo3 xs)

sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = (x+n):sumarN n xs

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

ultimo :: [Integer] -> Integer
ultimo [a] = a
ultimo (x:xs) = ultimo xs

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [a] = [a+a]
sumarElUltimo xs = sumarN (ultimo xs) xs

pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x : pares xs
             | otherwise = pares xs

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x : multiplosDeN n xs
                      | otherwise = multiplosDeN n xs

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar n (x:xs) | n == x = xs
                | otherwise = x : quitar n xs 

ordenar :: (Ord t) => [t] -> [t]
ordenar [] = []
ordenar xs = ordenar (quitar (maximo3 xs) xs) ++ [maximo3 xs]
-- ordenar lista = minimo lista : ordenar (quitar (minimo lista) lista)