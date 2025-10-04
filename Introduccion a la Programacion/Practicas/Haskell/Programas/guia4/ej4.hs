{--
Aqui hay que usar la formula de sumatoria de numeros impares (2k-1),
y encontrar la relacion de recurrencia (ver teorica)

problema sumaImpares(n: Z): Z {
    requiere: {n > 0}
    asegura: {resultado es la suma de los primeros n impares}
}
--}

sumaImpares :: Integer -> Integer
sumaImpares n | n == 1 = 1
              | otherwise = sumaImpares (n-1) + 2*n - 1