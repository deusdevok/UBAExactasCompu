{--
La idea de la recursion es comenzar por el numero en cuestion, por ejemplo 4.32
Para extraer la parte entera de forma recursiva, vamos hacia atras de uno en uno
En cada paso, vamos sumando 1, hasta llegar al 0 (caso base)
De esta manera, el resultado de ir sumando todos esos 1 da lo que buscamos

problema parteEntera (x: R): Z {
    requiere: {x >= 0}
    asegura: {resultado <= x < resultado + 1}
}
--}

parteEntera :: Float -> Integer
parteEntera x | x < 1 = 0
              | otherwise = 1 + parteEntera (x-1)