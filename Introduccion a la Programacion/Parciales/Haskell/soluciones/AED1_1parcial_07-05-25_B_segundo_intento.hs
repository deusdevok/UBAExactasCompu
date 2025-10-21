cantidadNumerosAbundantes :: Int -> Int -> Int
cantidadNumerosAbundantes d h
    | d > h = 0
    | esAbundante d = 1 + resto
    | otherwise = resto
    where resto = cantidadNumerosAbundantes (d+1) h

esAbundante :: Int -> Bool
esAbundante 1 = 1
esAbundante n = sumaDivPropios n > n

sumaDivPropios :: Int -> Int
sumaDivPropios n = sumaDivHasta n (n-1)

sumaDivHasta :: Int -> Int -> Int
sumaDivHasta n 1 = 1
sumaDivHasta n h
    | mod n h == 0 = h + resto
    | otherwise = resto
    where resto = sumaDivHasta n (h-1)