fact :: Integer -> Integer
fact 0 = 1
fact n = n*fact (n-1)

{--
problema eAprox (n: Z): R {
    requiere: {n >= 0}
    asegura: {resultado es la suma desde i=0 hasta n de 1/i!}
}
--}

eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n = 1/fromIntegral (fact n) + eAprox (n-1)

e :: Float
e = eAprox 10

f::Integer -> Integer
f x = x