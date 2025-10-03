{--
problema f1 (n: Z): Z {
    requiere: {n >= 0}
    asegura: {resultado es la suma desde i=0 hasta n de 2^i}
}
--}

f1 :: Integer -> Integer
f1 0 = 1
f1 n = 2^n + f1 (n-1)

{--
problema f2 (n: Z, q: R): R {
    requiere: {n > 0}
    asegura: {resultado es la suma desde i=1 hasta n de q^i}
}
--}

f2 :: Integer -> Float -> Float
f2 1 q = q
f2 n 0 = 0
f2 n q = q^n + f2 (n-1) q

{--
problema f3 (n: Z, q: R): R {
    requiere: {n >= 0}
    asegura: {resultado es la suma desde i=1 hasta 2n de q^i}
}
--}

f3 :: Integer -> Float -> Float
f3 0 q = 0
-- f3 1 q = q + q^2
f3 n q = q^(2*n) + q^(2*n-1) + f3 (n-1) q

{--
problema f4(n: Z, q: R): R {
    requiere: {n >= 0}
    asegura: {resultado es la suma desde i=n hasta 2n de q^i}
}
--}

f4 :: Integer -> Float -> Float
f4 _ 0 = 0
f4 0 _ = 1
f4 n q = q^(2*n) + q^(2*n-1) - q^(n-1) + f4 (n-1) q