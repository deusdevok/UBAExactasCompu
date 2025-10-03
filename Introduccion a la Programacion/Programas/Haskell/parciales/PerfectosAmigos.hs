divisoresPropiosHasta :: Int -> Int -> [Int]
divisoresPropiosHasta 1 1 = []
divisoresPropiosHasta _ 1 = [1]
divisoresPropiosHasta n m
    | mod n m == 0 = m : divisoresPropiosHasta n (m-1)
    | otherwise = divisoresPropiosHasta n (m-1)

divisoresPropios :: Int -> [Int]
divisoresPropios 1 = []
divisoresPropios n = divisoresPropiosHasta n (n-1)

sumaLista :: [Int] -> Int
sumaLista [] = 0
sumaLista (x:xs) = x + sumaLista xs

sumaDivisoresPropios :: Int -> Int
sumaDivisoresPropios n = sumaLista (divisoresPropios n)

sonAmigos :: Int -> Int -> Bool
sonAmigos n m = n /= m && n == sumaDivisoresPropios m && m == sumaDivisoresPropios n

esPerfecto :: Int -> Bool
esPerfecto 1 = True
esPerfecto n = n == sumaDivisoresPropios n

proxPerfectoDesde :: Int -> Int
proxPerfectoDesde 0 = 1
proxPerfectoDesde n
    | esPerfecto n = n
    | otherwise = proxPerfectoDesde (n+1)

nEsimoPerfecto :: Int -> Int
nEsimoPerfecto 1 = 1
nEsimoPerfecto n = proxPerfectoDesde (nEsimoPerfecto (n-1) + 1)

losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos 1 = [1]
losPrimerosNPerfectos n = losPrimerosNPerfectos (n-1) ++ [nEsimoPerfecto n]

paresConX :: Int -> [Int] -> [(Int, Int)]
paresConX x [] = []
paresConX x (y:ys)
    | sonAmigos x y = (x, y) : paresConX x ys
    | otherwise = paresConX x ys

combinaciones :: [Int] -> [Int] -> [(Int,Int)]
combinaciones [] _ = []
combinaciones _ [] = []
combinaciones (x:xs) (y:ys) = paresConX x (y:ys) ++ combinaciones xs ys

listaDeAmigos :: [Int] -> [(Int, Int)]
listaDeAmigos [] = []
listaDeAmigos [x] = []
listaDeAmigos xs = combinaciones xs xs

listaPosiblesAmigos = [1,2,3,220,4,5,6,284]