{--
Idea: La secuencia de Fibonacci empieza:
0 1 1 2 3 5 8 13 21 34 ...

Para chequear que un dado numero x pertenece a la secuencia de Fibonacci,
debemos de alguna manera generar la secuencia hasta coincidir con dicho numero
o hasta que nos pasemos.

Para esto podemos usar una funcion auxiliar (recursiva) "checkFibo"
Esta funcion chequea que a partir de dos Fibonacci, pueda llegar a un dado x y que sea de la secuencia

problema checkFibo (a: Z, b: Z, target: Z): Bool {
    requiere: {a >= 0, b >= 1, target >= 1}
    asegura: {resultado = true sii puedo llegar a target sumando a+b, generando Fibonacci. Si me paso, False}
}

problema esFibonacci (n: Z) : B {
    requiere: { n >= 0 }
    asegura: { resultado = true ↔ n es algun valor de la secuencia de Fibonacci definida en el ejercicio 1}
}
--}

esFibonacci :: Integer -> Bool
esFibonacci 0 = True
esFibonacci n = checkFibo 0 1 n

checkFibo :: Integer -> Integer -> Integer -> Bool
checkFibo a b target
    | b == target = True
    | b > target = False
    | otherwise = checkFibo b (a+b) target