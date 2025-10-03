{--
Parcial de Práctica - Introducción a la Programación (Haskell)

Ejercicio 1 (2 puntos)
problema promedioPrimosPosicionesPares (xs: seq⟨Z⟩) : Float {
  requiere: {|xs| > 0}
  asegura: {res es el promedio de los números primos que están en posiciones pares de xs (la primera posición es la 1)}
  asegura: {si no hay primos en posiciones pares, res = 0}
}

Ejercicio 2 (2 puntos)
problema esCrecienteIgnorandoBlancos (palabra: seq⟨Char⟩) : Bool {
  requiere: {True}
  asegura: {res = true <=> los caracteres no blancos de palabra están en orden estrictamente creciente}
}

Ejercicio 3 (2 puntos)
problema cantidadDeVecesQueAparece (x: Z, xs: seq⟨Z⟩) : Z {
  requiere: {True}
  asegura: {res es la cantidad de veces que x aparece en xs}
}

Ejercicio 4 (2 puntos)
problema sonPermutaciones (xs: seq⟨Z⟩, ys: seq⟨Z⟩) : Bool {
  requiere: {|xs| = |ys|}
  asegura: {res = true <=> xs es una permutación de ys (tienen los mismos elementos, en cualquier orden, con la misma cantidad de repeticiones)}
}

Ejercicio 5 (2 puntos)
problema sumaElementosFueraDeDiagonal (matriz: seq⟨seq⟨Z⟩⟩) : Z {
  requiere: {matriz es cuadrada}
  asegura: {res es la suma de todos los elementos que NO están en la diagonal principal}
}
--}

-- Problema 1

promedioPrimosPosicionesPares :: [Int] -> Float
promedioPrimosPosicionesPares xs = promedio (extraerPrimos (extraerElementosEnPosPares xs))

extraerElementosEnPosPares :: [Int] -> [Int]
extraerElementosEnPosPares [] = []
extraerElementosEnPosPares [x] = []
extraerElementosEnPosPares (x:y:es) = y : extraerElementosEnPosPares es

extraerPrimos :: [Int] -> [Int]
extraerPrimos [] = []
extraerPrimos (x:xs)
    | esPrimo x = x : extraerPrimos xs
    | otherwise = extraerPrimos xs

esPrimo :: Int -> Bool
esPrimo x = proximoDivisorDesde x 2 == x

proximoDivisorDesde :: Int -> Int -> Int
proximoDivisorDesde x d
    | d > x = error "divisor es mayor que dividendo"
    | mod x d == 0 = d
    | otherwise = proximoDivisorDesde x (d+1)

promedio :: [Int] -> Float
promedio [] = 0
promedio xs = fromIntegral (sumaElementos xs) / fromIntegral (longitud xs)

sumaElementos :: [Int] -> Int
sumaElementos [] = 0
sumaElementos (x:xs) = x + sumaElementos xs

longitud :: [Int] -> Int
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- Problema 2

esCrecienteIgnorandoBlancos :: [Char] -> Bool
esCrecienteIgnorandoBlancos [] = True
esCrecienteIgnorandoBlancos [x] = True
esCrecienteIgnorandoBlancos (' ':xs) = esCrecienteIgnorandoBlancos xs
esCrecienteIgnorandoBlancos (x:' ':xs) = esCrecienteIgnorandoBlancos (x:xs)
esCrecienteIgnorandoBlancos (x:y:xs)
    | x > y = False
    | otherwise = esCrecienteIgnorandoBlancos (y:xs)

-- Problema 3

cantidadDeVecesQueAparece :: Int -> [Int] -> Int
cantidadDeVecesQueAparece _ [] = 0
cantidadDeVecesQueAparece e (x:xs)
    | e == x = 1 + resto
    | otherwise = resto
    where resto = cantidadDeVecesQueAparece e xs

-- Ejercicio 4

-- Chequeo cantidadDeVecesQueAparece cada elemento de xs en xs y en ys y me fijo si coinciden
sonPermutaciones :: [Int] -> [Int] -> Bool
sonPermutaciones [] [] = True
sonPermutaciones (x:xs) ys
    | cantidadDeVecesQueAparece x (x:xs) == cantidadDeVecesQueAparece x ys = sonPermutaciones (quitarElem x xs) (quitarElem x ys)
    | otherwise = False

-- quitar todos los elementos e de una lista
quitarElem :: Int -> [Int] -> [Int]
quitarElem _ [] = []
quitarElem e (x:xs)
    | e == x = quitarElem e xs
    | otherwise = x : quitarElem e xs

-- Ejercicio 5

sumaElementosFueraDeDiagonal :: [[Int]] -> Int
sumaElementosFueraDeDiagonal [] = 0
sumaElementosFueraDeDiagonal xs = sumaAux xs 1 (long xs)

long :: [a] -> Int
long [] = 0
long (_:xs) = 1 + long xs

-- ayuda a mantener info del indice
sumaAux :: [[Int]] -> Int -> Int -> Int
sumaAux [] _ _ = 0
sumaAux xs i n | i > n = 0
sumaAux (x:xs) i n = sumaFilaNExcepto x i + sumaAux xs (i+1) n 

sumaFilaNExcepto :: [Int] -> Int -> Int
sumaFilaNExcepto xs i = sumaFila (quitarElementoEnIndice xs i)

sumaFila :: [Int] -> Int
sumaFila [] = 0
sumaFila (x:xs) = x + sumaFila xs

quitarElementoEnIndice :: [Int] -> Int -> [Int]
quitarElementoEnIndice xs i = quitarElementoEnIndiceAux xs i (long xs)

quitarElementoEnIndiceAux :: [Int] -> Int -> Int -> [Int]
quitarElementoEnIndiceAux (_:xs) 1 _ = xs
quitarElementoEnIndiceAux (x:xs) i n = x : quitarElementoEnIndiceAux xs (i-1) n

{--
Otra forma, quizas mejor, de quitar un elemento de una lista, dado un indice
quitarElementoDeLista :: Int -> [a] -> [a]
quitarElementoDeLista 1 (_:xs) = xs
quitarElementoDeLista n (e:xs) = e : quitarElementoDeLista (n-1) xs
--}