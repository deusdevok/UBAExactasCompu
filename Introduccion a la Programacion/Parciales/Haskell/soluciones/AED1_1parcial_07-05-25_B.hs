-- https://www.cubawiki.com.ar/images/d/d0/AED1_1parcial_07-05-25_B.pdf

-- Ejercicio 1

sumaDivisoresHasta :: Int -> Int -> Int
sumaDivisoresHasta n 1 = 1
sumaDivisoresHasta n m
    | mod n m == 0 = m + sumaDivisoresHasta n (m-1)
    | otherwise = sumaDivisoresHasta n (m-1)

sumaDivisoresPropios :: Int -> Int
sumaDivisoresPropios n = sumaDivisoresHasta n (n-1)

esAbundante :: Int -> Bool
esAbundante n = n < sumaDivisoresPropios n

cantidadNumerosAbundantes :: Int -> Int -> Int
cantidadNumerosAbundantes d h
    | h == 1 || h < d = 0
    | esAbundante h = 1 + cantidadNumerosAbundantes d (h-1)
    | otherwise = cantidadNumerosAbundantes d (h-1)

-- Ejercicio 2

-- [(nombre materia, anio aprobacion, cuatrimestre)]
cursadasVencidas :: [(String, Int, Int)] -> [String]
cursadasVencidas [] = []
cursadasVencidas ((materia, anio, cuatri):cs)
    | anio > 2021 || (anio == 2021 && cuatri >= 1) = cursadasVencidas cs
    | otherwise = materia : cursadasVencidas cs

-- Ejercicio 3

saturarEnUmbralHastaNegativo :: [Int] -> Int -> [Int]
saturarEnUmbralHastaNegativo [] _ = []
saturarEnUmbralHastaNegativo (x:xs) _ | x < 0 = []
saturarEnUmbralHastaNegativo (x:xs) u
    | x > u = u : saturarEnUmbralHastaNegativo xs u
    | otherwise = x : saturarEnUmbralHastaNegativo xs u

-- Ejercicio 4

iEsimoEnFila :: [Int] -> Int -> Int
iEsimoEnFila (x:_) 1 = x
iEsimoEnFila (_:xs) i = iEsimoEnFila xs (i-1)

extraerColumna :: [[Int]] -> Int -> [Int]
extraerColumna [] _ = []
extraerColumna (x:xs) col = iEsimoEnFila x col : extraerColumna xs col

cantidadParesLista :: [Int] -> Int
cantidadParesLista [] = 0
cantidadParesLista (x:xs)
    | mod x 2 == 0 = 1 + cantidadParesLista xs
    | otherwise = cantidadParesLista xs

cantidadParesColumna :: [[Int]] -> Int -> Int
cantidadParesColumna [] _ = 0
cantidadParesColumna matriz col = cantidadParesLista (extraerColumna matriz col)

-- Ejercicio 5

{--
Conteste marcando la opción correcta.
¿Qué ocurre si una definición por pattern matching no contempla todos los casos posibles?
(F) El programa no compila.
(F) Haskell elige un valor por defecto automáticamente.
(T) El programa puede lanzar un error en tiempo de ejecución si se invoca con un patrón no contemplado.
--}

-- Ejercicio 6

{--
Conteste marcando la opción correcta.
Dado un problema con parámetros c (de tipo Char) y s (de tipo String), cuya única precondición es (esVocal(c) ∨ longitud(s) > 3):
(F) La precondición garantiza que siempre se trabajará con strings no vacíos.
(T) Si c es una consonante y s tiene longitud igual a 2, no se garantiza el comportamiento correcto del programa.
(F) Cualquier combinación de valores de c y s es válida, porque la precondición es una disyunción en vez de una conjunción.
--}