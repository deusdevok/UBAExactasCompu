{--
Idea:
- Si el numero es menor que 10 (tiene un solo digito), entonces es capicua
- Si es menor que 100 (esta entre 10 y 99), chequeo que sea multiplo de 11. Si lo es, es capicua
- Si es mayor o igual que 100 (3 digitos o mas):
 - Si primer y ultimo digito son iguales, hago recursion quitando primer y ultimo digitos
 
problema esCapicua (n: Z): B {
    requiere: {n >= 0}
    asegura: {si n es capicua, res es True, sino False}
}
--}
primerDigito :: Integer -> Integer
primerDigito x | x < 10 = x
               | otherwise = primerDigito (div x 10)

ultimoDigito :: Integer -> Integer
ultimoDigito x = mod x 10

elimUnidad :: Integer -> Integer
elimUnidad x = div x 10

cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos (elimUnidad n)

esCapicua :: Integer -> Bool
esCapicua x | x < 10 = True
            | x < 100 = mod x 11 == 0
            | otherwise = primerDigito x == ultimoDigito x && esCapicua (div (mod x (10^(cantDigitos x - 1))) 10)