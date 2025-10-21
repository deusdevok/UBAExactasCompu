type Fila = [Int]
type Tablero = [Fila]
type Posicion = (Int, Int)
type Camino = [Posicion]

maxEntreDosNumeros :: Int -> Int -> Int
maxEntreDosNumeros x y
    | x >= y = x
    | otherwise = y

maximoEnFila :: Fila -> Int
maximoEnFila [x] = x
maximoEnFila (x:xs) = maxEntreDosNumeros x (maximoEnFila xs)

maximo :: Tablero -> Int
maximo [xs] = maximoEnFila xs
maximo (x:xs) = maxEntreDosNumeros (maximoEnFila x) (maximo xs)

cantAparicionesFila :: Int -> Fila -> Int
cantAparicionesFila _ [] = 0
cantAparicionesFila e (x:xs)
    | x == e = 1 + cantAparicionesFila e xs
    | otherwise = cantAparicionesFila e xs

cantAparicionesTablero :: Int -> Tablero -> Int
cantAparicionesTablero _ [] = 0
cantAparicionesTablero e (x:xs) = cantAparicionesFila e x + cantAparicionesTablero e xs

masRepetidoFila :: Fila -> Int
masRepetidoFila [x] = x
masRepetidoFila (x:xs)
    | cantAparicionesFila x (x:xs) >= cantAparicionesFila (masRepetidoFila xs) (x:xs) = x
    | otherwise = masRepetidoFila xs

-- ESTA MAL ESTO
-- [[1,2,2,4],[5,1,7,8],[9,10,1,12],[13,14,15,1]] da 2 y tiene que dar 1
masRepetido :: Tablero -> Int
masRepetido [x] = masRepetidoFila x
masRepetido (x:xs)
    | cantAparicionesTablero (masRepetidoFila x) (x:xs) >= cantAparicionesTablero (masRepetido xs) (x:xs) = masRepetidoFila x
    | otherwise = masRepetido xs



valoresDeCamino :: Tablero -> Camino -> [Int]
valoresDeCamino _ [(x,y)] = [x,y]
valoresDeCamino t ((x,y):cs) = x:y:valoresDeCamino t cs

fibo :: Int -> Int
fibo 0 = 0
fibo 1 = 1
fibo n = fibo (n-1) + fibo (n-2)

esFiboDesde :: Int -> Int -> Int -> Bool
esFiboDesde n a b
    | n == a || n == b = True
    | a > n = False
    | otherwise = esFiboDesde n b (a+b)

esFibo :: Int -> Bool
esFibo n = esFiboDesde n 0 1

esCaminoFibo :: [Int] -> Int -> Bool
esCaminoFibo [] _ = True
esCaminoFibo [x] n = x == n && esFibo x
esCaminoFibo (x:y:xs) n = x == n && esCaminoFiboAux (y:xs) x y

esCaminoFiboAux :: [Int] -> Int -> Int -> Bool
esCaminoFiboAux [] _ _ = True
esCaminoFiboAux [x] prev primero = x == primero
esCaminoFiboAux (x:xs) prev primero = x == primero && esCaminoFiboAux xs primero (prev + primero)