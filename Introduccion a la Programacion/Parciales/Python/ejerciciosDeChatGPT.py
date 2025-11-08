"""
Ejercicio 21. Parque de diversiones - Control de adrenalina

Cada juego del parque tiene un “nivel de adrenalina” entre 1 y 10.
Dada una secuencia con los niveles de los juegos que una persona visitó en el día, se pide una función que determine el intervalo más largo en el que la adrenalina fue estrictamente creciente.

problema maximo tramo creciente (in niveles: seq⟨Z⟩) : Z {
    requiere: {Todos los niveles están entre 1 y 10 inclusive.}
    requiere: {niveles no está vacío.}
    asegura: {res es la longitud máxima de un tramo consecutivo de niveles estrictamente creciente.}
}
"""

def maximo_tramo_creciente(niveles: list[int]) -> int:
    maximo_tramo_hasta_ahora: int = 0
    longitud_crecientes: int = 1
    for i in range(1, len(niveles)):
        if niveles[i] > niveles[i-1]:
            longitud_crecientes += 1
        else:
            maximo_tramo_hasta_ahora = maximo_entre_2(maximo_tramo_hasta_ahora, longitud_crecientes)
            longitud_crecientes = 1

    return maximo_entre_2(maximo_tramo_hasta_ahora, longitud_crecientes)

def maximo_entre_2(x, y):
    if x > y:
        return x
    return y

print(maximo_tramo_creciente([1,2,3,4,5,4,5,6,7,8,9,5,4,3]))