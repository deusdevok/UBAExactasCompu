an :: Integer -> Float
an 1 = 2
an n = 2 + 1/an (n-1)

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = an n - 1