pertenece :: Eq t => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs)
    | n == x = True
    | otherwise = pertenece n xs

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [_] = True
todosIguales (x:y:xs) | x /= y = False
                      | otherwise = todosIguales (y:xs)

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [_] = True
todosDistintos (x:y:xs) | x == y = False
                        | otherwise = todosDistintos (x:xs) && todosDistintos (y:xs)

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos [_] = False
hayRepetidos (x:y:xs) | x == y = True
                      | otherwise = hayRepetidos (x:xs) || hayRepetidos (y:xs)

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar n (x:xs) | n == x = xs
                | otherwise = x : quitar n xs 

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos n (x:xs) 
    | n == x = quitarTodos n xs
    | otherwise = x : quitarTodos n xs

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [a] = [a]
eliminarRepetidos (x:xs) | pertenece x xs = eliminarRepetidos xs
                         | otherwise = x : eliminarRepetidos xs



listaEnOtraLista :: Eq t => [t] -> [t] -> Bool
listaEnOtraLista [] _ = True
listaEnOtraLista (x:xs) ys
    | not (pertenece x ys) = False
    | otherwise = listaEnOtraLista xs ys

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] _ = True
mismosElementos _ [] = True
mismosElementos xs ys = 
    listaEnOtraLista xs ys && listaEnOtraLista ys xs

ultimo :: [t] -> t
ultimo [a] = a
ultimo (_:xs) = ultimo xs

principio :: [t] -> [t]
principio [_] = []
principio (x:xs) = x : principio xs

reverso :: [t] -> [t]
reverso [a] = [a]
reverso xs = ultimo xs : reverso (principio xs)

capicua :: (Eq t) => [t] -> Bool
capicua xs = xs == reverso xs