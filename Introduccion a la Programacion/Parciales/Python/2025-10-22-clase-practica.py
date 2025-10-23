"""
Camas ocupadas en el hospital
Queremos saber qué porcentaje de ocupación de camas hay en el hospital. El hospital se representa por una matriz en donde las filas son los pisos, y las columnas son las camas. Los valores de la matriz son booleanos que indican si la cama está ocupada o no. Si el valor es verdadero (True) indica que la cama está ocupada. Se nos pide programar en Python una función que devuelve una secuencia de enteros, indicando la proporción de camas ocupadas en cada piso.

problema nivel_de_ocupacion(camas_por_piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
  requiere: {Todos los pisos tienen la misma cantidad de camas.}
  requiere: {Hay por lo menos 1 piso en el hospital.}
  requiere: {Hay por lo menos una cama por piso.}
  asegura: {|res| = |camas|}
  asegura: {Para todo 0<= i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el total de camas del piso i)}
}
"""

def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    res: list[float] = []
    for piso in camas_por_piso:
        ocupacion = nivel_ocupacion_en_piso(piso)
        res.append(ocupacion)

    return res

def nivel_ocupacion_en_piso(piso: list[bool]) -> float:
    total: int = len(piso)
    ocupadas: int = 0
    for cama_ocupada in piso :
        ocupadas += uno_si_cero_si_no(cama_ocupada)

    porcentaje: float = ocupadas / total
    return porcentaje

def uno_si_cero_si_no(cond: bool) -> int:
    return 1 if cond else 0


# print(nivel_de_ocupacion([[True]])) # [1]
# print(nivel_de_ocupacion([[True,False,True],[False,False,True],[True,True,True],[False,False,False]])) # [2/3, 1/3, 3/3, 0/3]

"""
problema cambiar_matriz(inout A: seq seq int)
"""

def cambiar_matriz(A: list[list[int]]) -> list[list[int]]:
    rotar_lista(A)
    for fila in A:
        rotar_lista(fila)

def rotar_lista(fila: list[int]) -> list[int]:
    primer_elemento: int = fila.pop(0)
    fila.append(primer_elemento)

# mat = [[1,2]]
# cambiar_matriz(mat)
# print(mat)

# mat = [[1,2],[3,4]]
# cambiar_matriz(mat)
# print(mat)

# mat = [[1],[2],[3]]
# cambiar_matriz(mat)
# print(mat)
    
# mat = [[1,2,3],[4,5,6],[7,8,9]]
# cambiar_matriz(mat)
# print(mat)

"""
problema_de_salidas
"""

def problema_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    res: dict[str, tuple[int, float]] = {}
    for nombre, salidas in registro.items():
        salidas_validas = salidas_mayores_a_0_y_menor_61(salidas)
        res[nombre] = (len(salidas_validas), promedio_lista(salidas_validas))

    return res

def salidas_mayores_a_0_y_menor_61(salidas: list[int]):
    res: list[int] = []
    for salida in salidas:
        if salida > 0 and salida < 61:
            res.append(salida)

    return res


def promedio_lista(s: list[int]) -> float:
    total: int = 0
    for elem in s:
        total += elem

    promedio: float
    if len(s) > 0:
        promedio = total / len(s)
    else:
        promedio = 0
    return promedio
    


registro = {
    "a": [61,60,59,58],
    "b": [1,2,3,0]
}
print(problema_de_salidas(registro))
