longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs
-- longitud xs = 1 + longitud (tail xs)

ultimo :: [t] -> t
ultimo [a] = a
ultimo (_:xs) = ultimo xs
-- ultimo xs = ultimo (tail xs)

principio :: [t] -> [t]
principio [_] = []
principio (x:xs) = x : principio xs

reverso :: [t] -> [t]
reverso [a] = [a]
reverso xs = ultimo xs : reverso (principio xs)