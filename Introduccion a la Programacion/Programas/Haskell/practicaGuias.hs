-- Guia 3, Ejercicio 4

productoInterno :: (Float, Float) -> (Float, Float) -> Float
productoInterno (x1,y1) (x2,y2) = x1*x2 + y1*y2

esParMenor :: (Float, Float) -> (Float, Float) -> Bool
esParMenor (x1,y1) (x2,y2) = x1 < x2 && y1 < y2

distancia :: (Float, Float) -> (Float, Float) -> Float
distancia (x1,y1) (x2,y2) = sqrt ((x2-x1)^2 + (y2-y1)^2)

sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (x,y,z) = x+y+z

multiploONum :: Int -> Int -> Int
multiploONum a n
    | mod a n == 0 = a
    | otherwise = 0

sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (x,y,z) n = multiploONum x n + multiploONum y n + multiploONum z n

esPar :: Int -> Bool
esPar a = mod a 2 == 0

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (x,y,z)
    | esPar x = 1
    | esPar y = 2
    | esPar z = 3
    | otherwise = 4

crearPar :: a -> b -> (a,b)
crearPar x y = (x,y)

invertir :: (a,b) -> (b,a)
invertir (x,y) = (y,x)

-- Guia 4, Ejercicio 7

cantDigitos :: Integer -> Integer
cantDigitos n
    | n < 10 = 1
    | otherwise = 1 + cantDigitos (div n 10)

digitoUnidades :: Integer -> Integer
digitoUnidades n = mod n 10

elimUnidad :: Integer -> Integer
elimUnidad x = div x 10

iEsimoDigito :: Integer -> Integer -> Integer
iEsimoDigito n i
    | i == cantDigitos n = digitoUnidades n
    | otherwise = iEsimoDigito (elimUnidad n) i
    -- | otherwise = iEsimoDigito (div n 10) i -- De esta forma no funciona. Hay que usar funcion auxiliar elimUnidad, sino la recursion no corta.

-- Guia 4, Ejercicio 14

sumaInterna :: Integer -> Integer -> Integer -> Integer
sumaInterna q n 1 = q^(n+1)
sumaInterna q n m = q^(n+m) + sumaInterna q n (m-1)

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q 1 m = sumaInterna q 1 m
sumaPotencias q n m = sumaInterna q n m + sumaPotencias q (n-1) m

-- Guia 5, Ejercicio 1

longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

ultimo :: [t] -> t
ultimo [x] = x
ultimo (_:xs) = ultimo xs

principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs

reverso :: [t] -> [t]
reverso [] = []
reverso [x] = [x]
reverso (x:xs) = reverso xs ++ [x]

-- Guia 3, Ejercicio 8

sumaUltimosDosDigitos :: Int -> Int
sumaUltimosDosDigitos x = mod x 10 + mod (div x 10) 10

comparar :: Int -> Int -> Int
comparar a b
    | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
    | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
    | otherwise = 0

-- Guia 4, Ejercicio 2

parteEntera :: Float -> Integer
parteEntera x
    | x < 1 = 0
    | otherwise = 1 + parteEntera (x-1)

-- Guia 5, Ejercicio 7

type Texto = [Char]
type Identificacion = Integer
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
type Disponibilidad = Bool

existeElLocker :: Identificacion ->MapaDeLockers ->Bool
existeElLocker _ [] = False
existeElLocker id ((i,_):ls)
    | id == i = True
    | otherwise = existeElLocker id ls

ubicacionDelLocker :: Identificacion ->MapaDeLockers ->Ubicacion
ubicacionDelLocker _ [] = "Error al ubicar locker"
ubicacionDelLocker id ((i,(_,u)):ls)
    | id == i = u
    | otherwise = ubicacionDelLocker id ls

estaDisponibleElLocker :: Identificacion ->MapaDeLockers ->Bool
estaDisponibleElLocker _ [] = False
estaDisponibleElLocker id ((i,(d,_)):ls)
    | id == i = d
    | otherwise = estaDisponibleElLocker id ls

ocuparLocker :: Identificacion ->MapaDeLockers ->MapaDeLockers
ocuparLocker _ [] = []
ocuparLocker id ((i,(d,u)):ls)
    | id == i && d = (i,(False,u)):ls
    | otherwise = (i,(d,u)):ocuparLocker id ls

lockers :: MapaDeLockers
lockers = [
    (100,(False,"ZD39I")),
    (101,(True,"JAH3I")),
    (103,(True,"IQSA9")),
    (105,(True,"QOTSA")),
    (109,(False,"893JJ")),
    (110,(False,"99292"))
    ]
