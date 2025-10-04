{--
problema tomaValorMax (n1: Z, n2: Z): Z {
    requiere: {n1 >= 1, n2 >= n1}
    asegura: {
        resultado es un entero m, tal que: 
        n1 <= m <= n2
        suma de los divisores de m = maximo de suma divisores i para i entre n1 y n2
    }
}
--}

sumaDivisoresNHastaK :: Integer -> Integer -> Integer
sumaDivisoresNHastaK n 1 = 1
sumaDivisoresNHastaK n k 
    | mod n k == 0 = k + sumaDivisoresNHastaK n (k-1)
    | otherwise = sumaDivisoresNHastaK n (k-1)

sumaDivisores :: Integer -> Integer
sumaDivisores 1 = 1
sumaDivisores n = sumaDivisoresNHastaK n n

tomaValorMax :: Integer -> Integer -> Integer
tomaValorMax 1 1 = 1
tomaValorMax n1 n2 
    | n1 == n2 = sumaDivisores n1
    | sumaDivisores n1 > sumaDivisores n2 = tomaValorMax n1 (n2-1)
    | otherwise = tomaValorMax (n1+1) n2