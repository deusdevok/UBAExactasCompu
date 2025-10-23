# Segundo Parcial - Introducción a la Programación, 2C 2024
# Tema 2 - Turno mañana

# ----------------------------------------------------

# Ejercicio 1 (2,25 puntos)
# Implementar la función subsecuencia_mas_larga especificada (todos_consecutivos no es testeado)

# problema subsecuencia_mas_larga (in v: seq⟨Z⟩) : ZxZ {
#   requiere: { La longitud de v es distinto de 0 }
#   asegura: { Sea x la primera subsecuencia más larga en v tal que vale todos_consecutivos(x), la primera componente de res es igual a |x| y la segunda es igual al índice en v donde comenzaría x }
# }

# problema todos_consecutivos (in v: seq⟨Z⟩) : Bool {
#   asegura: { res == True <==> cada par de elementos adyacentes en v son números consecutivos, es decir, que su diferencia es igual a 1 }
# }

def subsecuencia_mas_larga(v: list[int]) -> tuple[int, int]:
    mas_larga_hasta_ahora: int = 1
    pos_mas_larga: int = 0
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            sub = subsecuencia(v, i, j)
            if todos_consecutivos(sub) and len(sub) > mas_larga_hasta_ahora:
                mas_larga_hasta_ahora = len(sub)
                pos_mas_larga = i

    return (mas_larga_hasta_ahora, pos_mas_larga)

def subsecuencia(v: list[int], i: int, j: int) -> list[int]:
    res = []
    for k in range(i, j+1):
        res.append(v[k])

    return res

def todos_consecutivos(s: list[int]) -> bool:
    res: bool = True
    for i in range(1, len(s)):
        if s[i] != s[i-1] + 1:
            res = False
    return res

# print(todos_consecutivos([2,3,4,5])) # True
# print(todos_consecutivos([4,5,6,8,9])) # False
# print(subsecuencia_mas_larga([1])) # (1, 0)
# print(subsecuencia_mas_larga([1,2,3])) # (3, 0)
# print(subsecuencia_mas_larga([1,2,3,2,3,4,5,6,7,14,15])) # (6, 3)
# print(subsecuencia_mas_larga([3,2,1])) # (1, 0)


# ----------------------------------------------------

# Ejercicio 2 (2,25 puntos)
# Ana tiene exámenes de respuesta Verdadero ó Falso. Ella sabe que en cada examen la cantidad 
# de respuestas correctas cuyo valor es Falso es igual a la cantidad de respuestas correctas 
# cuyo valor es Verdadero. Tenemos el historial de las respuestas de cada exámen dados por Ana 
# en una cola. En cada uno Ana respondió todas las preguntas.

# problema mejor_resultado_de_ana (in examenes: Cola⟨ seq⟨Bool⟩ ⟩) : seq⟨Z⟩ {
#   requiere:{ Cada elemento de examenes es no vacío y tiene longitud par }
#   asegura: { res tiene la misma cantidad de elementos que examenes }
#   asegura: { res[i] es igual a la máxima cantidad de respuestas correctas que Ana podría haber respondido en el i-ésimo exámen resuelto en examenes, para 0 <= i < cantidad de elementos de examenes }
# }

from queue import Queue as Cola

def mejor_resultado_de_ana(examenes: Cola[list[bool]]) -> list[int]:
    res: list[int] = []
    while not examenes.empty():
        examen = examenes.get()
        res.append(mejor_resultado(examen))

    return res

def mejor_resultado(examen: list[bool]) -> int:
    # Del total de resultados en examen, la mitad deberia ser True, y la otra mitad False
    cantidad_true = 0
    for resultado in examen:
        cantidad_true += uno_si_cero_si_no(resultado)
        # cantidad_true += resultado

    res = len(examen) - abs(cantidad_true - (len(examen) // 2))

    return res

def uno_si_cero_si_no(cond: bool) -> int:
    return 1 if cond else 0

examenes: Cola = Cola()
examenes.put([True, True, False, False]) # 4 (todas)
examenes.put([True, False, False, False]) # 3
examenes.put([True, True, True, False]) # 3 (una menos)
examenes.put([True, True, True, True]) # 2 (la mitad del total)

print(mejor_resultado_de_ana(examenes))


# ----------------------------------------------------

# Ejercicio 3 (2,25 puntos)
# problema cambiar_matriz(inout A: seq⟨seq⟨Z⟩⟩) {
#   requiere: { Todas las filas de A tienen la misma longitud }
#   requiere: { El mínimo número que aparece en A es igual a 1 }
#   requiere: { El máximo número que aparece en A es igual a #filas de A por #columnas de A }
#   requiere: { No hay enteros repetidos en A }
#   requiere: { Existen al menos dos enteros distintos en A }
#   modifica: { A }
#   asegura: { A tiene exactamente las mismas dimensiones que A@pre }
#   asegura: { El conjunto de elementos que aparecen en A es igual al conjunto de elementos que aparecen en A@pre }
#   asegura: { A[i][j] != A@pre[i][j] para todo i, j en rango }
# }

# Mi estrategia va a ser "rotar" cada fila, mandando el primer elemento al final.
# Por ejemplo: [1,2,3,4] -> [2,3,4,1]

def cambiar_matriz(A: list[list[int]]):
    for fila in range(len(A)):
        A[fila] = rotar_fila(A[fila])

def rotar_fila(f: list[int]):
    res: list[int] = []
    for i in range(1, len(f)):
        res.append(f[i])

    res.append(f[0])

    return res

# mat = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

# cambiar_matriz(mat)
# print(mat)

# ----------------------------------------------------

# Ejercicio 4 (2,25 puntos)
# Tenemos un texto que contiene palabras. Por simplicidad, las palabras están separadas únicamente por uno o más espacios.

# problema palabras_por_vocales (in texto: string): Diccionario⟨Z,Z⟩ {
#   requiere: { Si existe una letra vocal en texto, esta no lleva tildes, diéresis, ni ningún otro símbolo }
#   asegura: { Si existe una palabra en texto con x vocales en total, x es clave de res }
#   asegura: { Las claves de res representan la cantidad total de vocales de una palabra, y cada valor corresponde a la cantidad de palabras en texto con ese número de vocales. }
#   asegura: { Los valores de res son positivos }
# }

def palabras_por_vocales(texto: str) -> dict[int, int]:
    d: dict[int, int] = {}
    palabras: list[str] = extraer_palabras(texto)
    for palabra in palabras:
        n = cantidad_vocales(palabra)
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1

    return d

def extraer_palabras(s: str) -> list[str]:
    palabras: list[str] = []
    palabra = ""
    for c in s:
        if c != " ":
            palabra += c
        else:
            if len(palabra) > 0:
                palabras.append(palabra)
                palabra = ""
    if len(palabra) > 0:
        palabras.append(palabra)

    return palabras

def cantidad_vocales(s: str) -> int:
    cant: int = 0
    vocales = "aeiou"
    for c in s:
        if pertenece(vocales, c):
            cant += 1

    return cant

def pertenece(s: str, c: str) -> bool:
    res: bool = False
    for k in s:
        if k == c:
            res = True

    return res

# print(cantidad_vocales("hola"))
# print(extraer_palabras("   hola   como estas      "))
# print(palabras_por_vocales("   hola   como estas    cosararaesteejercicio no?  "))

# ----------------------------------------------------

# Ejercicio 5 (1 punto)
# ¿Por qué en Paradigma Imperativo no existe la transparencia referencial?
# [ ] Utilizamos otro mecanismo de repetición de código, en lugar de recursión usamos la iteración (FOR, WHILE, DO WHILE).
# [x] Tenemos una nueva instrucción, la asignación, que nos permite cambiar el valor de una variable
# [ ] El orden en que se ejecutan las instrucciones del programa es diferente