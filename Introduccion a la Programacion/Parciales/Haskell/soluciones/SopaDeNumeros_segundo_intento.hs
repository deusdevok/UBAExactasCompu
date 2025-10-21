type Fila = [Int]
type Tablero = [Fila]
type Posicion = (Int, Int)
type Camino = [Posicion]

maximo :: Tablero -> Int
maximo [t] = maximoEnFila t
maximo (t:ts) = maximoEntreDos (maximoEnFila t) (maximo ts)

maximoEntreDos :: Int -> Int -> Int
maximoEntreDos x y
    | x >= y = x
    | otherwise = y

maximoEnFila :: Fila -> Int
maximoEnFila [e] = e
maximoEnFila (e:es) = maximoEntreDos e (maximoEnFila es)

-- Caso de prueba (tiene que dar 1): [[1,2,2,4],[5,1,7,8],[9,10,1,12],[13,14,15,1]]
masRepetido :: Tablero -> Int
masRepetido t = masRepetidoEnFila (aplanar t)

masRepetidoEnFila :: Fila -> Int
masRepetidoEnFila [e] = e
masRepetidoEnFila (x:xs)
    | cantidadAparicionesFila x (x:xs) >= cantidadAparicionesFila (masRepetidoEnFila xs) (x:xs) = x
    | otherwise = masRepetidoEnFila xs


cantidadAparicionesFila :: Int -> Fila -> Int
cantidadAparicionesFila _ [] = 0
cantidadAparicionesFila e (x:xs)
    | e == x = 1 + resto
    | otherwise = resto
    where resto = cantidadAparicionesFila e xs

-- aplanar :: Tablero -> Fila
aplanar :: [[a]] -> [a]
aplanar [] = []
aplanar (t:ts) = t ++ aplanar ts


-- valoresDeCamino [[1,2,2,4],[5,1,7,8],[9,10,1,12],[13,14,15,1]] [(2,1),(2,2),(3,2),(3,3),(4,3)]
-- valoresDeCamino [[1]] [(1,1)]
valoresDeCamino :: Tablero -> Camino -> [Int]
valoresDeCamino _ [] = []
valoresDeCamino ts ((x,y):cs) = extraerElementoDeTablero x y ts : valoresDeCamino ts cs

extraerElementoDeTablero :: Int -> Int -> Tablero -> Int
extraerElementoDeTablero x y ts = extraerElemento y (extraerElemento x ts)

extraerElemento :: Int -> [a] -> a
extraerElemento 1 (e:_) = e
extraerElemento n (e:xs) = extraerElemento (n-1) xs

quitarElementoDeLista :: Int -> [a] -> [a]
quitarElementoDeLista 1 (_:xs) = xs
quitarElementoDeLista n (e:xs) = e : quitarElementoDeLista (n-1) xs

-- 1 1 2 3 5 8 13 21 34 ...
-- [3,5,8,13] 4 da true
esCaminoFibo :: [Int] -> Int -> Bool
esCaminoFibo [] _ = False
esCaminoFibo [x] n = x == fibo n
esCaminoFibo (x:xs) n
    | x /= fibo n = False
    | otherwise = esCaminoFibo xs (n+1)

fibo :: Int -> Int
fibo 1 = 1
fibo 2 = 1
fibo n = fibo (n-1) + fibo (n-2)

-- Probar:
-- esCaminoFibo (valoresDeCamino tablero [(3,2), (4, 2), (4,3)]) 3
tablero :: Tablero
tablero = [
    [13,12,6,4],
    [1,1,32,25],
    [9,2,14,7],
    [7,3,5,16],
    [27,2,8,18]
    ]