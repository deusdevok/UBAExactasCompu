{--
Yo: Carlos Prado
Certifico que el siguiente archivo fue elaborado únicamente por mí, sin ayuda de otras personas o herramientas.
--}


module SolucionT2 where

-- Ejercicio 1
mayorNumeroConNDivisores :: Integer -> Integer -> Integer -> Integer
mayorNumeroConNDivisores d h n
    | h < d = 0
    | numeroDivisores h == n = h
    | otherwise = mayorNumeroConNDivisores d (h-1) n

numeroDivisores :: Integer -> Integer
numeroDivisores n = numeroDivisoresHasta n n

numeroDivisoresHasta :: Integer -> Integer -> Integer
numeroDivisoresHasta n 1 = 1
numeroDivisoresHasta n h
    | mod n h == 0 = 1 + numeroDivisoresHasta n (h-1)
    | otherwise = numeroDivisoresHasta n (h-1)

-- Ejercicio 2
sanguchitoDeCerosMasGrande :: [Integer] -> Integer
sanguchitoDeCerosMasGrande xs = sangucheMasGrandeEntre xs 2 (longitud xs - 1)

sangucheMasGrandeEntre :: [Integer] -> Integer -> Integer -> Integer
sangucheMasGrandeEntre (x:xs) d h
    | d > h = 0
    | esSanguchitoDeCeros (x:xs) d = maximo (elemento (x:xs) d) resto
    | otherwise = resto
    where resto = sangucheMasGrandeEntre (x:xs) (d+1) h

elemento :: [Integer] -> Integer -> Integer
elemento (x:xs) 1 = x
elemento (x:xs) n = elemento xs (n-1)

esSanguchitoDeCeros :: [Integer] -> Integer -> Bool
esSanguchitoDeCeros (x:y:[]) _ = False
esSanguchitoDeCeros xs 0 = False
esSanguchitoDeCeros (x:y:z:xs) i
    | i >= (longitud (x:y:z:xs)) = False
    | i == 2 && x == 0 && z == 0 = True
    | otherwise = esSanguchitoDeCeros (y:z:xs) (i-1)

longitud :: [Integer] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

maximo :: Integer -> Integer -> Integer
maximo x y
    | x > y = x
    | otherwise = y

-- Ejercicio 3
agruparPorCantidadDeTemporadas :: [(String, Integer)] -> [(Integer, [String])]
agruparPorCantidadDeTemporadas [] = []
agruparPorCantidadDeTemporadas ((nombre, cantTemporadas):series) = agregarOActualizar nombre cantTemporadas (agruparPorCantidadDeTemporadas series)

agregarOActualizar :: String -> Integer -> [(Integer, [String])] -> [(Integer, [String])]
agregarOActualizar nombre cantTemporadas [] = [(cantTemporadas, [nombre])]
agregarOActualizar nombre cantTemporadas ((c,nombres):series)
    | cantTemporadas == c = ((c,(nombre:nombres)):series)
    | otherwise = (c,nombres) : agregarOActualizar nombre cantTemporadas series

-- Ejercicio 4
reemplazarMinimoDeCadaFila :: [[Integer]] -> Integer -> [[Integer]]
reemplazarMinimoDeCadaFila [] _ = []
reemplazarMinimoDeCadaFila (x:xs) n = reemplazarMinimoFila x n : reemplazarMinimoDeCadaFila xs n

reemplazarMinimoFila :: [Integer] -> Integer -> [Integer]
reemplazarMinimoFila xs n = reemplazarNporMEnFila (minimoFila xs) n xs

reemplazarNporMEnFila :: Integer -> Integer -> [Integer] -> [Integer]
reemplazarNporMEnFila _ _ [] = []
reemplazarNporMEnFila n m (x:xs)
    | x == n = m : reemplazarNporMEnFila n m xs
    | otherwise = x : reemplazarNporMEnFila n m xs

minimoFila :: [Integer] -> Integer
minimoFila [x] = x
minimoFila (x:xs)
    | x < minimoFila xs = x
    | otherwise = minimoFila xs

{--
Siendo la última modificación con la solución final:
COMPLETE FECHA y HORA DE ULTIMA MODIFICACIÓN ACA
1 de Octubre de 2025, 19:43
--}
