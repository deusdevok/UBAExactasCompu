type Punto3D = (Float, Float, Float)

valorAbsoluto :: Float -> Float
valorAbsoluto a | a < 0 = -a
                | otherwise = a

distanciaManhattan :: Punto3D -> Punto3D -> Float
distanciaManhattan (x1, y1, z1) (x2, y2, z2) = valorAbsoluto (x2-x1) +
                                               valorAbsoluto (y2-y1) +
                                               valorAbsoluto (z2-z1)