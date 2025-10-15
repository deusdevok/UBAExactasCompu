from typing import TypeVar

T = TypeVar("T")

# Ejercicio 1

def pertenece1(s: list[T], e: T) -> bool:
    return e in s

def pertenece2(s: list[int], e: int) -> bool:
    for x in s:
        if x == e:
            return True
        
    return False

def pertenece3(s: list[int], e: int) -> bool:
    i = 0
    while i < len(s):
        if s[i] == e:
            return True
        i += 1
        
    return False

def pertenece4(s, e):
    i: int = 0
    while (len(s) > i and s[i] != e):
        i += 1

    return i == len(s)

def divide_a_todos(s: list[int], e: int) -> bool:
    for elem in s:
        if elem % e != 0:
            return False
        
    return True

def suma_total(s: list[int]) -> int:
    total: int = 0
    for elem in s:
        total += elem

    return total

def maximo(s: list[int]) -> int:
    maximo_hasta_ahora: int = s[0]
    for i in range(1, len(s)):
        if s[i] > maximo_hasta_ahora:
            maximo_hasta_ahora = s[i]

    return maximo_hasta_ahora

def minimo(s: list[int]) -> int:
    minimo_hasta_ahora: int = s[0]
    for i in range(1, len(s)):
        if s[i] < minimo_hasta_ahora:
            minimo_hasta_ahora = s[i]

    return minimo_hasta_ahora

def ordenados(s: list[int]) -> bool:
    ordenados: bool = True
    for i in range(1, len(s)):
        if s[i-1] > s[i]:
            ordenados = False
    
    return ordenados

def pos_maximo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    
    maximo_hasta_ahora: int = s[0]
    pos: int = 0
    for i in range(1, len(s)):
        if s[i] > maximo_hasta_ahora:
            maximo_hasta_ahora = s[i]
            pos = i

    return pos

def pos_minimo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    
    minimo_hasta_ahora: int = s[0]
    pos: int = 0
    for i in range(1, len(s)):
        if s[i] < minimo_hasta_ahora:
            minimo_hasta_ahora = s[i]
            pos = i

    return pos

def long_mayorASiete(s: list[str]) -> bool:
    es_mayor_a_7: bool = False
    for palabra in s:
        if len(palabra) > 7:
            es_mayor_a_7 = True

    return es_mayor_a_7

def es_palindroma(s: str) -> bool:
    palindroma: bool = True
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            palindroma = False
        
    return palindroma

def iguales_consecutivos(s: list[int]) -> bool:
    stack: list[int] = []
    consecutivos: bool = False
    for n in s:
        if len(stack) != 0 and stack[-1] != n:
            stack.clear()
        
        stack.append(n)

        if len(stack) >= 3:
            consecutivos = True

    return consecutivos

def vocales_distintas(s: str) -> bool:
    vocales: list[str] = ["a","e","i","o","u"]
    vocales_en_s: list[str] = []
    for c in s:
        if pertenece1(vocales, c) and not pertenece1(vocales_en_s, c):
            vocales_en_s.append(c)

    return len(vocales_en_s) >= 3

def pos_secuencia_ordenada_mas_larga(s: list[int]) -> int:
    posicion_cadena_mas_larga: int = 0
    posicion_actual: int = 0
    maxima_longitud_actual: int = 0
    maxima_longitud_global: int = 0
    for i in range(1, len(s)):
        if s[i] >= s[i-1]:
            maxima_longitud_actual += 1
        else:
            if maxima_longitud_actual > maxima_longitud_global:
                maxima_longitud_global = maxima_longitud_actual
                posicion_cadena_mas_larga = posicion_actual

            maxima_longitud_actual = 0
            posicion_actual = i

    return posicion_cadena_mas_larga

def cantidad_impares(n: int) -> int:
    total_impares: int = 0
    while n > 0:
        ultimo_digito = n%10
        if ultimo_digito%2 != 0:
            total_impares += 1
        n //= 10

    return total_impares

def cantidad_digitos_impares(s: list[int]) -> int:
    total_impares: int = 0
    for e in s:
        total_impares += cantidad_impares(e)

    return total_impares



## Ejercicio 2

def CerosEnPosicionesPares(s: list[int]) -> None: # No hace falta poner -> None (para procedimientos)
    for i in range(0, len(s), 2):
        s[i] = 0

def CerosEnPosicionesPares2(s: list[int]) -> list[int]:
    s_copy = s.copy()
    for i in range(0, len(s_copy), 2):
        s_copy[i] = 0

    return s_copy

def sin_vocales(s: str) -> str:
    vocales = "aeiouAEIOU"
    palabra_sin_vocales = ""
    for c in s:
        if not pertenece1(vocales, c):
            palabra_sin_vocales += c

    return palabra_sin_vocales

def reemplaza_vocales(s: str) -> str:
    # reemplazar vocales por guion bajo
    vocales = "aeiouAEIOU"
    palabra_reemplazada: str = ""
    for c in s:
        if pertenece1(vocales, c):
            palabra_reemplazada += "_"
        else:
            palabra_reemplazada += c

    return palabra_reemplazada

def da_vuelta_str(s: str) -> str:
    string_dado_vuelta: str = ""
    for i in range(len(s)-1, -1, -1):
        string_dado_vuelta += s[i]

    return string_dado_vuelta

def eliminar_repetidos(s: str) -> str:
    sin_repes: str = ""
    for c in s:
        if not pertenece1(sin_repes, c):
            sin_repes += c

    return sin_repes

## Ejercicio 3

def resultadoMateria(notas: list[int]) -> int:
    promedio: float = 0
    for nota in notas:
        promedio += nota

    promedio /= len(notas)

    res: int
    if promedio >= 7:
        res = 1
    elif 4 <= promedio < 7:
        res = 2
    else:
        res = 3

    return res

## Ejercicio 4

def saldoActual(movimientos: list[(str, int)]) -> int:
    saldo = 0
    for (tipo, cantidad) in movimientos:
        if tipo == "I":
            saldo += cantidad
        elif tipo == "R":
            if saldo < cantidad:
                saldo = 0
            else:
                saldo -= cantidad

    return saldo

## Ejercicio 5

def pertenece_a_cada_uno_version_1(s: list[list[int]], e: int, res: list[bool]):
    for i in range(len(s)):
        if i < len(res):
            res[i] = pertenece1(s[i], e)
        else:
            res.append(pertenece1(s[i], e))

def pertenece_a_cada_uno_version_2(s: list[list[int]], e: int, res: list[bool]):
    res.clear()
    for i in range(len(s)):
        res.append(pertenece1(s[i], e))

def pertenece_a_cada_uno_version_3(s: list[list[int]], e: int) -> list[bool]:
    res: list[bool] = []
    for i in range(len(s)):
        res.append(pertenece1(s[i], e))

    return res

"""
Relacion de fuerza: a es mas fuerte que b, si y solo si
a -> b es una tautologia

a | b | a -> b
--------------
T | T |   T
T | F |   F <- esta no va!
F | T |   T
F | F |   T

a: pertenece_a_cada_uno_version_2 -> |res| == |s|
b: pertenece_a_cada_uno_version_1 -> |res| >= |s|

De aqui podemos ver que "a C b" (a esta contenido en b)

Por lo tanto, podemos decir que version2 es mas fuerte que version1

Puedo usar la especificacion de 2 para la 1
"""

## Ejercicio 6

def es_matriz(s: list[list[int]]) -> bool:
    res: bool = True
    if len(s) > 0 and len(s[0]) > 0:
        longitud_primer_fila: int = len(s[0])
        for i in range(1, len(s)):
            if len(s[i]) != longitud_primer_fila:
                res = False
    else:
        res = False

    return res

def filas_ordenadas(m: list[list[int]], res: list[bool]):
    res.clear()
    for i in range(len(m)):
        res.append(ordenados(m[i]))

def columna(m: list[list[int]], c: int) -> list[int]:
    columna: list[int] = []
    for fila in m:
        columna.append(fila[c])

    return columna

def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
    res: list[bool] = []
    for col in range(len(m[0])):
        res.append(ordenados(columna(m, col)))

    return res

def transponer(m: list[list[int]]) -> list[list[int]]:
    res = []
    for col in range(len(m[0])):
        res.append(columna(m, col))

    return res

def quien_gana_tateti(m: list[list[int]]) -> int:
    """
    ganador puede ser 0, 1 o 2
    0: gana O
    1: gana X
    2: hay empate
    """
    ganador: int = 2 # Por defecto hay empate

    # Recorro filas
    for fila in m:
        if fila == ["O","O","O"]:
            ganador = 0
        elif fila == ["X","X","X"]:
            ganador = 1

    # Recorro columnas
    for col in range(len(m[0])):
        colu = columna(m, col)
        if colu == ["O","O","O"]:
            ganador = 0
        elif colu == ["X","X","X"]:
            ganador = 1

    # Diagonal principal
    diag_1 = [m[0][0], m[1][1], m[2][2]]
    if diag_1 == ["O","O","O"]:
        ganador = 0
    elif diag_1 == ["X","X","X"]:
        ganador = 1

    # Diagonal cruzada
    diag_2 = [m[0][2], m[1][1], m[2][0]]
    if diag_2 == ["O","O","O"]:
        ganador = 0
    elif diag_2 == ["X","X","X"]:
        ganador = 1

    return ganador

#########################
# EXPONENCIACION MATRIZ #
#########################

def multiplicar_listas(a: list[int], b: list[int]) -> int:
    # producto interno entre dos filas del mismo tamanio
    res: int = 0
    for i in range(len(a)):
        res += a[i] * b[i]

    return res

def generar_matriz_cuadrada_random(d: int) -> list[list[float]]:
    import numpy as np
    m = np.random.random((d, d))

    return m

def exponenciacion_matriz(d: int, p: int) -> list[list[float]]:
    # Comienzo probando con una matriz hardcodeada
    # TODO: generar matriz random (cuadrada)

    # m = [[1,1,1],[1,1,1],[1,1,1]]
    m = generar_matriz_cuadrada_random(d)

    for _ in range(p):
        res: list[list[float]] = []

        # Voy calculando fila a fila
        for f in range(len(m)):
            fila = [] # Inicializo resultado para cada fila
            # Recorro columna
            for c in range(len(m[0])):
                # Estoy en la posicion (f,c) del resultado
                # Ahora hago el calculo de (fila x columna)
                fila.append(multiplicar_listas(m[f], columna(m, c)))

            res.append(fila)

        m = res

    return res

a = exponenciacion_matriz(200,3)
print(a)