-- EJERCICIO 1 (2 puntos)
-- problema mediaMovilN (lista: seq⟨Z⟩, n: Z) : Float {
--   requiere: {|lista| > 0}
--   requiere: {n > 0 ∧ n ≤ |lista|}
--   asegura: {res es el promedio de los últimos n elementos de lista}
-- }

mediaMovilN :: [Int] -> Int -> Float
mediaMovilN [e] _ = fromIntegral e
mediaMovilN xs n = fromIntegral (suma (ultimosN xs n)) / fromIntegral n

suma :: [Int] -> Int
suma [] = 0
suma (x:xs) = x + suma xs

ultimosN :: [Int] -> Int -> [Int]
ultimosN (x:xs) n
    | longitud (x:xs) <= n = (x:xs)
    | otherwise = ultimosN xs n

longitud :: [Int] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

-- EJERCICIO 2 (2 puntos)
-- problema esAtractivo (n: Z) : Bool {
--   requiere: {n > 0}
--   asegura: {res = true <=> la cantidad de factores primos de n (distintos o no)
-- es también un número primo.}
-- }
-- Aclaración: los factores primos de 30 son [5,3,2]. Los factores primos de 9 son [3,3]. 

esAtractivo :: Int -> Bool
esAtractivo n = esPrimo (longitud (factoresPrimos n))

-- longitud esta definido en el Ejercicio 1

esPrimo :: Int -> Bool
esPrimo 1 = False
esPrimo n = proximoDivisorDesde n 2 == n

proximoDivisorDesde :: Int -> Int -> Int
proximoDivisorDesde n d
    | mod n d == 0 || n == d = d
    | otherwise = proximoDivisorDesde n (d+1)

factoresPrimos :: Int -> [Int]
factoresPrimos 1 = []
factoresPrimos n = primerDivPrimo : factoresPrimos (div n (primerDivPrimo))
    where primerDivPrimo = primerDivisorPrimoDesde n 2

primerDivisorPrimoDesde :: Int -> Int -> Int
primerDivisorPrimoDesde n d
    | not (esPrimo d) || mod n d /= 0 = primerDivisorPrimoDesde n (d+1)
    | otherwise = d

-- EJERCICIO 3 (2 puntos)
-- problema palabraOrdenada (palabra: seq⟨Char⟩) : Bool {
--   requiere: {True}
--   asegura: {res = true <=> cada uno de los elementos no blancos de palabra es mayor o igual al anterior caracter no blanco, si existe alguno.}
-- }
-- Aclaración: 'a' < 'b' es True. 

-- EJERCICIO 4 (3 puntos)
-- problema similAnagrama (palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Bool⟩{
--   requiere: {True}
--   asegura: {res = true <=> (para todo caracter no blanco, la cantidad de apariciones de ese caracter en palabra1 es igual a la cantidad de apariciones en palabra2, y además existe al menos un caracter en palabra1 que tiene una posición distinta en palabra2)}
-- }