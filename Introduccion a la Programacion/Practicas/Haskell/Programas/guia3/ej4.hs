-- Ejercicio 4

{--
a)

problema productoInterno (primeraLista: RxR, segundaLista: RxR): R {
    requiere: {True}
    asegura: {res es el producto interno entre ambas listas}
}
--}
productoInterno :: (Float, Float) -> (Float, Float) -> Float
productoInterno (a,b) (c,d) = a*c + b*d
-- productoInterno tupla1 tupla2 = fst tupla1 * fst tupla2 + snd tupla1 * snd tupla2

{--
b)

problema esParMenor (t1: RxR, t2: RxR): Bool {
    requiere: {True}
    asegura: {res es True si primer elemento de t1 es menor que primero de t2, y lo mismo con la segunda de cada una}
}
--}
esParMenor :: (Float, Float) -> (Float, Float) -> Bool
esParMenor (a, b) (c, d) = a < c && b < d

{--
c) Distancia Euclidea

problema distancia (P1: RxR, P2: RxR): R {
    requiere: {True}
    asegura: {res es un numero real mayor o igual que cero}
    asegura: {res es la distancia entre P2 y P2, usando norma 2}
}
--}
distancia :: (Float, Float) -> (Float, Float) -> Float
distancia (x1, y1) (x2, y2) = sqrt ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))

{--
d)

problema sumaTerna (n: RxRxR): R {
    requiere: {True}
    asegura: {res es la suma de los tres elementos de n}
}
--}
sumaTerna :: (Float, Float, Float) -> Float
sumaTerna (a, b, c) = a + b + c

{--
e) sumar solo multiplos
problema sumarSoloMultiplos (numeros: ZxZxZ, n: Z): R {
    requiere: {True}
    asegura: {res es la suma de los elementos de la terna numeros, tales que sean multiplos de n}
}

problema multiploONum (a: Z, b: Z): Z {
    requiere: {True}
    asegura: {res es a si a es multiplo de b}
    asegura: {res es 0 si a no es multiplo de b}
}
--}
esMultiplo :: Integer -> Integer -> Bool
esMultiplo num n = mod num n == 0

multiploONum :: Integer -> Integer -> Integer
multiploONum num n | esMultiplo num n = num
                   | otherwise = 0

sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) n = multiploONum a n + multiploONum b n + multiploONum c n

{--
f)
problema posPrimerPar (numeros: ZxZxZ): Z {
    requiere: {True}
    asegura: {res es la posicion (contando desde 1) del primer elemento par en numeros}
    asegura: {si no hay ningun elemento par en numeros, res es 4}
}
--}
esPar :: Integer -> Bool
esPar n = mod n 2 == 0

posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (a, b, c) | esPar a = 1
                       | esPar b = 2
                       | esPar c = 3
                       | otherwise = 4

{--
g)
problema crearPar (a, b): axb {
    requiere: {True}
    asegura: {res es una Tupla con componentes (a, b)}
}
--}
crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

{--
h)
problema invertir ()
--}
invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)

{--
i)
--}
type Punto2D = (Float, Float)

productoInterno2 :: Punto2D -> Punto2D -> Float
productoInterno2 (a,b) (c,d) = a*c + b*d

esParMenor2 :: Punto2D -> Punto2D -> Bool
esParMenor2 (a, b) (c, d) = a < c && b < d

distancia2 :: Punto2D -> Punto2D -> Float
distancia2 (x1, y1) (x2, y2) = sqrt ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
