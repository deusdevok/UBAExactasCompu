maximoEntreDos :: (Ord a) => a -> a-> a
maximoEntreDos x y
    | x > y = x
    | otherwise = y

maximo :: (Ord a) => [a] -> a
maximo [x] = x
maximo (x:xs) = maximoEntreDos x (maximo xs)

maximo2 :: (Ord a) => [a] -> a
maximo2 [] = error "caca"
maximo2 [x] = x
maximo2 (x:xs)
    | x > maximo2 xs = x
    | otherwise = maximo2 xs

replicate' :: Int -> Int -> [Int]
replicate' 0 _ = []
replicate' n a = a : replicate' (n-1) a

take' :: (Num i, Ord i) => i -> [a] -> [a]
take' n _
    | n <= 0 = []
take' _ [] = []
take' n (x:xs) = x : take' (n-1) xs

reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]

repeat' :: a -> [a]
repeat' x = x : repeat' x

zip' :: [a] -> [b] -> [(a, b)]
zip' _ [] = []
zip' [] _ = []
zip' (x:xs) (y:ys) = (x, y) : zip' xs ys

elem' :: (Eq a) => a -> [a] -> Bool
elem' _ [] = False
elem' e (x:xs) = e == x || elem' e xs

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
-- quicksort (x:xs) = quicksort [a | a <- xs, a <= x] ++ [x] ++ quicksort [a | a <- xs, a > x]
quicksort (x:xs) =
    let smallerSorted = quicksort [a | a <- xs, a <= x]
        biggerSorted = quicksort [a | a <- xs, a > x]
    in smallerSorted ++ [x] ++ biggerSorted
    -- in biggerSorted ++ [x] ++ smallerSorted -- Para ordenar de mayor a menor

