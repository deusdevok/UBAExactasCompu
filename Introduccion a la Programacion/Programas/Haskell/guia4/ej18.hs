{--
problema mayorDigitoPar (n: N) : N {
    requiere: { True }
    asegura: { resultado es el mayor de los digitos pares de n. Si n no tiene ningun digito par, entonces resultado es -1. }
}
--}

esPar :: Integer -> Bool
esPar x = mod x 2 == 0

digitoUnidades :: Integer -> Integer
digitoUnidades x = mod x 10

elimUnidad :: Integer -> Integer
elimUnidad x = div x 10

mayorPar :: Integer -> Integer -> Integer
mayorPar a b | not (esPar a) && not (esPar b) = -1
             | not (esPar a) && esPar b = b
             | esPar a && not (esPar b) = a
             | a > b = a
             | otherwise = b

mayorDigitoPar :: Integer -> Integer
mayorDigitoPar x 
    | x < 10 && esPar x = x
    | x < 10 = -1
    | otherwise = mayorPar (digitoUnidades x) (mayorDigitoPar (elimUnidad x))