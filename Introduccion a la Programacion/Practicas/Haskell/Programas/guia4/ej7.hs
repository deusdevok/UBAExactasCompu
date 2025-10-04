
{--
problema iesimoDigito (n: Z, i: Z) : Z {
    requiere: { n >= 0 ∧ 1 <= i <= cantDigitos(n) }
    asegura: { resultado = (n div 10^{cantDigitos(n)−i}) mod 10 }
}

problema cantDigitos (n: Z) : N {
    requiere: { n >= 0 }
    asegura: { n = 0 → resultado = 1}
    asegura: { n != 0 → (n div 10^{resultado−1} > 0 ∧ n div 10^{resultado} = 0) }
}
--}

digitoUnidades :: Integer -> Integer
digitoUnidades x = mod x 10

elimUnidad :: Integer -> Integer
elimUnidad x = div x 10

cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos (elimUnidad n)

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | i == cantDigitos n = digitoUnidades n
                 | otherwise = iesimoDigito (elimUnidad n) i
                 -- | otherwise = iEsimoDigito (div n 10) i -- De esta forma no funciona. Hay que usar funcion auxiliar elimUnidad, sino la recursion no corta.