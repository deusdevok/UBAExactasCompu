{--
En este problema simplemente aplicamos la definicion de fibonacci como funcion partida

fib(n) = {
        0 si n = 0
        1 si n = 1
        fib(n-1) + fib(n-2) en otro caso
    }

problema fibonacci (n: Z): Z {
    requiere: {n>=0}
    asegura: {resultado = fib(n)}
}
--}

fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)