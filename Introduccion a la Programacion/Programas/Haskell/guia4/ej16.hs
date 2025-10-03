{--
Implementar menorDivisor :: Integer -> Integer 
que calcule el menor divisor (mayor que 1) de un natural n pasado como parametro.

La funcion primerDivisorDesdeM toma dos parametros: n y m
Si m es divisible por n, devuelve m
En otro caso, hace recursion sumando uno a m
Es decir, devuelve el primer divisor de n, a partir de m

La funcion menorDivisor llama a la funcion primerDivisorDesdeM con el parametro n, y 2
Esto hace que empiece a buscar divisores empezando desde 2, y terminando
cuando encuentre el primer divisor, es decir el menor
--}

primerDivisorDesdeM :: Integer -> Integer -> Integer
primerDivisorDesdeM n m 
    | mod n m == 0 = m
    | otherwise = primerDivisorDesdeM n (m+1)

menorDivisor :: Integer -> Integer
menorDivisor n = primerDivisorDesdeM n 2

esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n

sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos 1 _ = True
sonCoprimos a b 
    | mod b (menorDivisor a) == 0 = False
    | otherwise = sonCoprimos (div a (menorDivisor a)) b

primerPrimoDesde :: Integer -> Integer
primerPrimoDesde x
    | esPrimo x = x
    | otherwise = primerPrimoDesde (x+1)

nEsimoPrimo :: Integer -> Integer
nEsimoPrimo 1 = 2
nEsimoPrimo x = primerPrimoDesde (nEsimoPrimo (x-1) + 1)
