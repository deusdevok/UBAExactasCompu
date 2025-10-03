sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [x] = [x]
sumaAcumulada (x:y:xs) = x : sumaAcumulada ((x+y):xs)

descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = primos x 2 : descomponerEnPrimos xs

{--
problema primos (x: Z): seq<Z> {
    requiere: {x >= 2}
    asegura: {resultado es una lista de enteros primos unicos}
    asegura: {multiplicar todos los elementos de resultado da el valor de x}
}
--}
primos :: Integer -> Integer -> [Integer]
primos x d
    | x == d = [x]
    | mod x d == 0 = d : primos (div x d) 2
    | otherwise = primos x (d+1)