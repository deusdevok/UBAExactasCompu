{--
problema sumaDigitos (n: Z): N {
    requiere: {n >= 0}
    asegura: {n < 10 -> n}
    asegura: {n >= 10 -> suma de los digitos}
}
--}

digitoUnidades :: Integer -> Integer
digitoUnidades x = mod x 10

quitarUnidad :: Integer -> Integer
quitarUnidad x = div x 10

sumaDigitos :: Integer -> Integer
sumaDigitos n | n < 10 = n
              | otherwise = sumaDigitos (quitarUnidad n) + digitoUnidades n