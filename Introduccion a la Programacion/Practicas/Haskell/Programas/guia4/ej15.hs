sumaInterna :: Integer -> Integer -> Float
sumaInterna a 1 = fromIntegral a
sumaInterna a m = fromIntegral a/fromIntegral m + sumaInterna a (m-1)

sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 1 m = sumaInterna 1 m
sumaRacionales n m = sumaInterna n m + sumaRacionales (n-1) m