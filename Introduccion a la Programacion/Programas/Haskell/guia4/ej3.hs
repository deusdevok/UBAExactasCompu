{--
Hay dos casos base: si a < b, no puede ser divisible. Si a == b, a es divisible por b
En otro caso (a > b), vamos reduciendo a (le restamos b), y volvemos a chequear si es divisible por b
Pueden pasar dos cosas: o nos pasamos, y queda que el primero es mas chico, entonces no es divisible,
o queda justo igual el primero con el segundo, cosa que es divisible
En cualquier caso, nos aseguramos de que uno de los dos casos base se va a cumplir

problema esDivisible(a: Z, b: Z): Bool {
    requiere: {a > 0}
    requiere: {b > 0}
    asegura: {resultado es True si a es divisible por b, sino False}
}
--}

esDivisible :: Integer -> Integer -> Bool
esDivisible a b | a < b = False
                | a == b = True
                | otherwise = esDivisible (a-b) b