sumaInterna :: Integer -> Integer -> Integer -> Integer
sumaInterna q a 1 = q^(a+1)
sumaInterna q a m = q^(a+m) + sumaInterna q a (m-1)

{--
problema sumaPotencias (q: Z, n: Z, m: Z): Z {
    requiere: {q >= 1, n >= 1, m >= 1}
    asegura: {resultado es la suma doble (para a entre 1 y n, b entre 1 y m) de q^(a+b)}
}
--}

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q 1 m = sumaInterna q 1 m
sumaPotencias q n m = sumaPotencias q (n-1) m + sumaInterna q n m