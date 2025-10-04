-- Ejercicio 1

{--
problema hayPrimosGemelos (d: Z,h: Z) : Bool {
  requiere: {0 < d ≤ h}
  asegura: {res = true <=> existen dos números p1 y p2 contenidos en el rango [d..h] tales que p1 y p2 son primos gemelos}
}

Aclaración: Se dice que p1 y p2 son primos gemelos si ambos son primos y además |p2-p1| = 2
--}

primerDivisorDesde :: Int -> Int -> Int
primerDivisorDesde n m
    | m > n = error "error en primerDivisorDesde: divisor mayor que el dividendo"
    | mod n m == 0 = m
    | n == m = n
    | otherwise = primerDivisorDesde n (m+1)

esPrimo :: Int -> Bool
esPrimo 1 = False
esPrimo n = n == primerDivisorDesde n 2

hayPrimosGemelos :: Int -> Int -> Bool
hayPrimosGemelos d h
    | h < d = error "Entrada invalida"
    | h - d < 2 = False
    | esPrimo d && esPrimo (d+2) = True
    | otherwise = hayPrimosGemelos (d+1) h

-- Ejercicio 2

{--
Representaremos un día de cursada de cierta materia con una tupla String x String x Z x Z, donde:

    La primera componente de la tupla contiene el nombre de una materia
    La segunda componente de la tupla contiene el día de cursada (lunes, martes, etc)
    La tercera componente de la tupla contiene el horario de inicio de la cursada de ese día
    La cuarta componente de la tupla contiene el horario de fin de la cursada de ese día

Se pide implementar materiasTurnoTarde, que dada una lista de cursadas devuelva aquellas materias que se cursan en el turno tarde (14 a 17hs)

problema materiasTurnoTarde (s: seq⟨String x String x Z x Z⟩) :seq⟨String⟩ {
  requiere: { s[i]1 es alguno de los siguientes valores: "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"}
  requiere: { s[i]2 ≥ 8 para todo i tal que 0 ≤ i < |s|}
  requiere: { s[i]3 ≤ 22 para todo i tal que 0 ≤ i < |s|}
  requiere: { s[i]2 < s[i]3 para todo i tal que 0 ≤ i < |s|}
  asegura: { res no tiene elementos repetidos}
  asegura: { res contiene los nombre de todas las materias incluídas en s tales el horario de cursada de dichas materias se superpone (total o parcialmente) con el rango (14..17)}
  
  asegura: { res contiene solamente los nombre las materias incluídas en s tales el horario de cursada de dichas materias se superpone (total o parcialmente) con el rango (14..17)}
}
--}

type Materia = String
type Dia = String
type HoraInicio = Int
type HoraFin = Int
type DiaDeCursada = (Materia, Dia, HoraInicio, HoraFin)
type Cursadas = [DiaDeCursada]

materiaEnLista :: Materia -> [Materia] -> Bool
materiaEnLista _ [] = False
materiaEnLista materia (m:ms) = materia == m || materiaEnLista materia ms

-- agrega una materia nueva, o superpone si ya existe
agregarMateria :: Materia -> [Materia] -> [Materia]
agregarMateria mat [] = [mat]
agregarMateria mat (m:ms)
  | mat == m = (m:ms)
  | otherwise = m : agregarMateria mat ms

materiaEnTurnoTarde :: Int -> Int -> Bool
materiaEnTurnoTarde i f = not ((i < 14 && f < 14) || (i > 17 && f > 17))

materiasTurnoTarde :: Cursadas -> [Materia]
materiasTurnoTarde [] = []
materiasTurnoTarde ((materia, _, inicio, fin):cursadas)
  | materiaEnTurnoTarde inicio fin = agregarMateria materia (materiasTurnoTarde cursadas)
  | otherwise = materiasTurnoTarde cursadas

cursadas :: Cursadas
cursadas = [
  ("programacion", "lunes", 15, 16),
  ("plp", "viernes", 18, 20),
  ("fisica", "martes", 13, 16),
  ("mate", "miercoles", 15, 18),
  ("algebra", "jueves", 13, 18),
  ("algoritmos", "viernes", 10, 12)
  ]

-- Ejercicio 3

{--
problema maximaSumaDeTresConsecutivos (s: seq⟨Z⟩) : Z {
  requiere: { |s| ≥ 3}
  asegura: { res es la suma de tres elementos que se encuentran en posiciones consecutivas de s }
  asegura: {Para cualquier i en el rango 1 ≤ i < |s|-1, se cumple que s[i-1]+s[i]+s[i+1] ≤ res}
}
--}

maximaSumaDeTresConsecutivos :: [Int] -> Int
maximaSumaDeTresConsecutivos [x,y,z] = x+y+z
maximaSumaDeTresConsecutivos (x:y:z:tail)
  | x+y+z > cola = x+y+z
  | otherwise = cola
  where cola = maximaSumaDeTresConsecutivos (y:z:tail)


-- Ejercicio 4

{--
problema sumaIesimaColumna (matriz: seq⟨seq⟨Integer⟩⟩, col: Integer) : Integer⟩{
  requiere: {Todos los elementos de la secuencia matriz tienen la misma longitud}
  requiere: {|matriz| > 0}
  requiere: {|matriz[0]| > 0}
  requiere: {1 ≤ col ≤ |matriz[0]| }
  asegura: {res es la sumatoria de los elementos matriz[i][col-1] para todo i tal que 0 ≤ i < |matriz| }
--}

iEsimoElemento :: [Int] -> Int -> Int
iEsimoElemento (x:xs) 1 = x
iEsimoElemento (x:xs) i = iEsimoElemento xs (i-1)

sumaIesimaColumna :: [[Int]] -> Int -> Int
sumaIesimaColumna [] _ = 0
sumaIesimaColumna (x:xs) i = iEsimoElemento x i + sumaIesimaColumna xs i

-- Ejercicio 5

{--
Conteste marcando la opción correcta.
Sean e1 y e2 dos especificaciones con la misma postcondición. Si la precondición de e1 es más débil que la de e2, entonces:
[X] Para que un programa sea correcto respecto de e2, debe considerar mayor cantidad de valores de entrada que un programa que busca satisfacer e1.
[ ] Para que un programa sea correcto respecto de e1, debe considerar mayor cantidad de valores de entrada que un programa que busca satisfacer e2.
[ ] No es posible afirmar ninguna de las opciones sin conocer en detalle ambas precondiciones.
--}


-- Ejercicio 6

{--
Conteste marcando la opción correcta.
Dado un problema con parámetros x e y, cuya precondición es (x>0 ∨ esPar(y)):
[ ] Todos los casos de test deben tener inputs que cumplan x>0 ∧ esPar(y)
[X] Independientemente de la precondición, debo testear todas las combinaciones de valores x e y
[ ] No tiene sentido tener un caso de test con x=0, y=1
--}