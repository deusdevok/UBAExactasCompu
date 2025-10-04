sumaInterna :: Integer -> Integer -> Integer
sumaInterna 0 _ = 0
sumaInterna n 1 = n
sumaInterna n m = n^m + sumaInterna n (m-1)

sumaDoble :: Integer -> Integer -> Integer
sumaDoble 0 _ = 0
-- sumaDoble 1 m = m
sumaDoble n 0 = n
sumaDoble n m = sumaDoble (n-1) m + sumaInterna n m