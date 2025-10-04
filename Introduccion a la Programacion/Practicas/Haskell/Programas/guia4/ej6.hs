{--
Si n < 10, entonces n tiene un solo digito, devuelvo True
Si n > 10, tengo al menos dos digitos. Checkeo que los ultimos dos digitos sean iguales.
Si ambos son iguales, hago recursion sobre el numero con un digito menos (div n 10)

problema todosDigitosIguales (n: Z) : B {
    requiere: { n > 0 }
    asegura: { resultado = true ↔ todos los digitos de n son iguales }
}
--}

digitoUnidades :: Integer -> Integer
digitoUnidades x = mod x 10

digitoDecenas :: Integer -> Integer
digitoDecenas x = mod (div x 10) 10

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = digitoUnidades n == digitoDecenas n && todosDigitosIguales (div n 10)