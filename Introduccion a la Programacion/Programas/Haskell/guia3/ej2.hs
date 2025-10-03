-- Ejercicio 2

{--
problema absoluto (n: Z): Z {
    requiere: {True}
    asegura: {res es mayor o igual que cero}
    asegura: {si n es positivo o cero, res es n}
    asegura: {si n es negativo, res es -n}
}
--}
absoluto :: Int -> Int
absoluto n | n>=0 = n
           | otherwise = -n

{--
problema maximoAbsoluto (x,y: Z): Z {
    requiere: {True}
    asegura: {res es mayor o igual que cero}
    asegura: {si absoluto x es mayor que absoluto y, res es absoluto x}
    asegura: {en otro caso, res es absoluto y}
}
--}
maximoAbsoluto :: Int -> Int -> Int
maximoAbsoluto x y | absoluto x > absoluto y = absoluto x
                   | otherwise = absoluto y

{--
problema maximo3 (x,y,z: Z): Z {
    requiere: {True}
    asegura: {si absoluto x mayor que maximoAbsoluto y z, res es absoluto x}
    asegura: {si absoluto y mayor que maximoAbsoluto x z, res es absoluto y}
    asegura: {si absoluto z mayor que maximoAbsoluto x y, res es absoluto z}
}
--}
maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z | absoluto x > maximoAbsoluto y z = absoluto x
              | absoluto y > maximoAbsoluto x z = absoluto y
              | absoluto z > maximoAbsoluto x y = absoluto z

{--
problema algunoEsCero (x,y: Q): Bool {
    requiere: {True}
    asegura: {si x o y es igual a 0, res es True, sino False}
}
--}
algunoEsCero :: Rational -> Rational -> Bool
algunoEsCero x y = x == 0 || y == 0

algunoEsCeroPatMatch :: Rational -> Rational -> Bool
algunoEsCeroPatMatch x 0 = True
algunoEsCeroPatMatch 0 y = True
algunoEsCeroPatMatch x y = False

{--
problema ambosSonCero (x,y: Q): Bool {
    requiere: {True}
    asegura: {si x e y son cero, res es True, sino False}
}
--}
ambosSonCero :: Rational -> Rational -> Bool
ambosSonCero x y = x == 0 && y == 0

ambosSonCeroPatMatch :: Rational -> Rational -> Bool
ambosSonCeroPatMatch 0 0 = True
ambosSonCeroPatMatch x y = False

{--
problema esMismoIntervalo (x,y: R): Bool {
    requiere: {True}
    asegura: {res es True si x e y pertenecen al mismo intervalo, sino False}
}
--}
esMismoIntervalo :: Double -> Double -> Bool
esMismoIntervalo x y = (x <= 3 && y <= 3) ||
                       (x > 3 && x <= 7 && y > 3 && y <= 7) ||
                       (x > 7 && y > 7)

{--
problema sumaDistintos (x,y,z: Z): Z {
    requiere: {True}
    asegura: {res es la suma de x,y,z, descartando los repetidos}
}
--}
sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | x == y && x == z = 0
                    | x == y = z
                    | x == z = y
                    | y == z = x
                    | otherwise = x + y + z


{--
problema esMultiploDe (x,y: Z): Bool {
    requiere: {True}
    asegura: {res es True si x es multiplo de y, sino False}
}
--}
esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y = mod x y == 0


{--
problema digitoUnidades (x: Z): Z {
    requiere: {True}
    asegura: {res es el ultimo digito de x, es decir, la unidad}
}
--}
digitoUnidades :: Int -> Int
digitoUnidades x = mod x 10


{--
problema digitoDecenas (x: Z): Z {
    requiere: {x > 9}
    asegura: {res es el ante ultimo digito de x, es decir, la decena}
}
--}
digitoDecenas :: Int -> Int
digitoDecenas x = mod (div x 10) 10