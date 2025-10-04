todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (a, b, c) | f a <= g a = False
                       | f b <= g b = False
                       | f c <= g c = False
                       | otherwise = True

f :: Integer -> Integer
f n | n <= 7 = n*n
    | n > 7 = 2*n - 1

g :: Integer -> Integer
g n | mod n 2 == 0 = div n 2
    | otherwise = 3*n + 1