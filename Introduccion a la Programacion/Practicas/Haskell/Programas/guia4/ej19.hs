-- primerDivisorDesdeM :: Integer -> Integer -> Integer
-- primerDivisorDesdeM n m 
--     | mod n m == 0 = m
--     | otherwise = primerDivisorDesdeM n (m+1)

-- menorDivisor :: Integer -> Integer
-- menorDivisor n = primerDivisorDesdeM n 2

-- esPrimo :: Integer -> Bool
-- esPrimo n = menorDivisor n == n

-- primerPrimoDesde :: Integer -> Integer
-- primerPrimoDesde x | esPrimo x = x
--                    | otherwise = primerPrimoDesde (x+1)

-- iEsimoPrimo :: Integer -> Integer
-- iEsimoPrimo 1 = 2
-- iEsimoPrimo n = primerPrimoDesde (iEsimoPrimo (n-1) + 1)

-- sumaPrimerosNPrimos 1 = 2
-- sumaPrimerosNPrimos n = sumaPrimerosNPrimos (n-1) + iEsimoPrimo n

-- esSumaInicialDeKPrimos :: Integer -> Integer -> Bool
-- esSumaInicialDeKPrimos x n | x == sumaPrimerosNPrimos n = True
--                            | x < sumaPrimerosNPrimos n = False
--                            | otherwise = esSumaInicialDeKPrimos x (n+1)


---------------------------------

{--
problema esSumaInicialDePrimos (n: Z) : B {
    requiere: { n >= 0 }
    asegura: { resultado = true ↔ n es igual a la suma de los m primeros numeros primos, para algun m.}
}
--}

primerDivisorDesdeM :: Integer -> Integer -> Integer
primerDivisorDesdeM n m 
    | n == m = n
    | mod n m == 0 = m
    | otherwise = primerDivisorDesdeM n (m+1)


esPrimo :: Integer -> Bool
esPrimo n = primerDivisorDesdeM n 2 == n

primerPrimoDesde :: Integer -> Integer
primerPrimoDesde x 
    | x == 1 = 2
    | esPrimo x = x
    | otherwise = primerPrimoDesde (x+1)


iEsimoPrimo :: Integer -> Integer
iEsimoPrimo 1 = 2
iEsimoPrimo i = primerPrimoDesde (iEsimoPrimo (i-1) + 1)

sumaPrimerosKPrimos :: Integer -> Integer
sumaPrimerosKPrimos 1 = 2
sumaPrimerosKPrimos k = iEsimoPrimo k + sumaPrimerosKPrimos (k-1)

esSumaInicialDeKPrimos :: Integer -> Integer -> Bool
esSumaInicialDeKPrimos x k
    | x == sumaPrimerosKPrimos k = True
    | x < sumaPrimerosKPrimos k = False
    | otherwise = esSumaInicialDeKPrimos x (k+1)

esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos x = esSumaInicialDeKPrimos x 1