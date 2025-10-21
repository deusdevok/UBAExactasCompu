actualizarStock :: String -> [(String, Int)] -> [(String, Int)]
actualizarStock "" stock = stock
actualizarStock x [] = [(x, 1)]
actualizarStock x ((nombre, cantidad):stocks)
    | x == nombre = (nombre, cantidad+1) : stocks
    | otherwise = (nombre, cantidad) : actualizarStock x stocks

generarStock :: [String] -> [(String, Int)]
generarStock [] = []
generarStock [x] = [(x, 1)]
generarStock (x:xs) = actualizarStock x (generarStock xs)

stockDeProducto :: [(String, Int)] -> String -> Int
stockDeProducto [] _ = 0
stockDeProducto ((p, n):xs) prod
    | p == prod = n
    | otherwise = stockDeProducto xs prod


precioDeProducto :: String -> [(String, Float)] -> Float
precioDeProducto _ [] = 0
precioDeProducto nombre ((n, precio):ps)
    | nombre == n = precio
    | otherwise = precioDeProducto nombre ps

dineroEnStock :: [(String, Int)] -> [(String, Float)] -> Float
dineroEnStock [] _ = 0
dineroEnStock ((nombre, cant):ss) precios = fromIntegral cant * precioDeProducto nombre precios + dineroEnStock ss precios

aplicarOferta :: [(String, Int)] -> [(String, Float)] -> [(String, Float)]
aplicarOferta [] precios = precios
aplicarOferta stock [] = []
aplicarOferta stock ((nombre, precio):ps)
    | stockDeProducto stock nombre > 10 = (nombre, precio * 0.8) : aplicarOferta stock ps
    | otherwise = (nombre, precio) : aplicarOferta stock ps


mercaderia = ["silla", "mesa", "silla", "lampara", "lampara", "cama", "lampara"]
stock = [("mesa",2),("lampara",10),("silla",3)]
precios = [("silla", 40.50), ("banquito", 30), ("mesa", 10), ("lampara", 1.40), ("cosa", 9.14)]