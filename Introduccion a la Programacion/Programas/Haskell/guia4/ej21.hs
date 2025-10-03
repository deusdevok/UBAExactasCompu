{--
problema pitagoras (m,n,r: Z): Z {
    requiere: {m,n,r >= 0}
    asegura: {
        resultado es la cantidad de pares (p,q), con 0 <= p <= m, 0 <= q <= n,
        tal que p^2 + q^2 <= r^2
    }
}
--}

checkPitagoras :: (Num a, Ord a) => a -> a -> a -> Bool
checkPitagoras x y r = x^2 + y^2 <= r^2

pitagorasInterno :: Integer -> Integer -> Integer -> Integer
pitagorasInterno m 0 r 
    | m <= r = 1
    | otherwise = 0
pitagorasInterno m n r 
    | checkPitagoras m n r = 1 + pitagorasInterno m (n-1) r
    | otherwise = pitagorasInterno m (n-1) r

pitagoras :: Integer -> Integer -> Integer -> Integer
pitagoras 0 n r = pitagorasInterno 0 n r
pitagoras m n r = pitagoras (m-1) n r + pitagorasInterno m n r