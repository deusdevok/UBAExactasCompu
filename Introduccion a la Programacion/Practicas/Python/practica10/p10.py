from queue import Queue as Cola
from typing import TypeVar
T = TypeVar('T')

## Ejercicio 1
## Esta mal el enunciado? Dice que devuelve list[int], pero el enunciado habla de diccionario

def stock_productos(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
    """
    requiere: cada elemento en stock_cambios contiene un string no vacio y un entero no negativo.

    ej: stock_cambios=[("comida", 3), ("huesito", 0), ("mantita", 5), ("comida", 1)]

    asegura: devuelve un diccionario. La clave es el nombre del producto, el valor es una tupla con el minimo y maximo stock historico registrado.
    """
    res: dict[str, tuple[int, int]] = {}
    for stock in stock_cambios:
        producto = stock[0]
        cantidad = stock[1]
        agregar_o_actualizar_producto(res, producto, cantidad)

    return res
        

def agregar_o_actualizar_producto(res: dict[str, tuple[int, int]], producto: str, cantidad: int):
    """
    modifica res
    """
    if producto not in res:
        res[producto] = (cantidad, cantidad)
    else:
        res[producto] = actualizar_minimo_y_maximo_en_tupla(res[producto], cantidad)

def actualizar_minimo_y_maximo_en_tupla(min_max: tuple[int, int], cantidad: int) -> tuple[int, int]:
    """
    requiere: min_max contiene solo dos elementos, y el primero es <= al segundo

    asegura: devuelve una tupla reemplazando el primer o segundo elemento con cantidad, segun si esta es menor al primero, o mayor al segundo
    """
    res: tuple[int, int] = min_max
    if cantidad < min_max[0]:
        res = (cantidad, min_max[1])
    elif cantidad > min_max[1]:
        res = (min_max[0], cantidad)

    return res

## Ejercicio 2

def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    res: list[int] = []
    for codigo in codigos_barra:
        if es_primo(ultimos_tres_digitos(codigo)):
            res.append(codigo)

    return res

def es_primo(n: int) -> bool:
    return primer_divisor_mayor_a_uno(n) == n

def primer_divisor_mayor_a_uno(n: int) -> int:
    res: int = n
    for i in range(n-1, 1, -1):
        if n%i == 0:
            res = i

    return res

def ultimos_tres_digitos(n: int) -> int:
    return n%1000

## Ejercicio 3
# Subsecuencia mas larga: probar todas las posibilidades (fuerza bruta) usando dos for anidados, usando subtarea para el segundo for, etc.

def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    mas_larga_hasta_ahora: int = 0
    indice_mayor: int = 0
    total = len(tipos_pacientes_atendidos)
    for i in range(total):
        long = longitud_perro_gato_desde_comienzo(tipos_pacientes_atendidos)
        if long > mas_larga_hasta_ahora:
            mas_larga_hasta_ahora = long
            indice_mayor = i
        tipos_pacientes_atendidos.pop(0)

    return indice_mayor

def longitud_perro_gato_desde_comienzo(lista: list[str]) -> int:
    res: int = 0
    subsecuencia = []
    for elem in lista:
        subsecuencia.append(elem)
        if es_subsecuencia_gato_perro(subsecuencia):
            res += 1

    return res

def es_subsecuencia_gato_perro(lista: list[str]) -> bool:
    """
    res es True si todos los elementos de lista son o "gato" o "perro"
    """
    res: bool = True
    for k in lista:
        if k != "gato" and k != "perro":
            res = False

    return res

## Ejercicio 4

def un_responsable_por_turno(grilla_horaria: list[list[str]]) -> list[tuple[bool, bool]]:
    res: list[tuple[bool, bool]] = []
    cantidad_columnas: int = len(grilla_horaria[0])

    for col in range(cantidad_columnas):
        columna = extraer_columna(col, grilla_horaria)
        turno_maniana = primeros_cuatro(columna)
        turno_tarde = ultimos_cuatro(columna)

        res.append((todos_iguales(turno_maniana), todos_iguales(turno_tarde)))

    return res

def extraer_columna(indice: int, matriz: list[list[T]]) -> list[T]:
    res: list[T] = []
    for row in matriz:
        res.append(row[indice])

    return res

def primeros_cuatro(columna: list[T]) -> list[T]:
    res: list[T] = []
    for i in range(4):
        res.append(columna[i])

    return res

def ultimos_cuatro(columna: list[T]) -> list[T]:
    res: list[T] = []
    for i in range(4, 8):
        res.append(columna[i])

    return res

def todos_iguales(columna: list[T]) -> bool:
    res: bool = True
    primer_elem: T = columna[0]
    for elem in columna:
        if elem != primer_elem:
            res = False
    
    return res

## Ejercicio 5

def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    res: dict[str, tuple[int, float]] = {}
    for nombre, salas in registro.items():
        salas_exitosas = salas_en_tiempo_cumplido(salas)
        salas_exito = len(salas_exitosas)
        promedio = promedio_salas(salas_exitosas)
        res[nombre] = (salas_exito, promedio)

    return res

def salas_en_tiempo_cumplido(salas: list[int]) -> list[int]:
    res: list[int] = []
    for sala in salas:
        if sala > 0 and sala <= 60:
            res.append(sala)

    return res

def promedio_salas(salas: list[int]) -> float:
    res: float = 0
    for tiempo in salas:
        res += tiempo

    if len(salas) > 0:
        res /= len(salas)
    else:
        res = 0.0

    return res

## Ejercicio 6

def tiempo_mas_rapido(tiempos_salas: list[int]) -> int:
    indice_mayor: int = 0
    mayor_tiempo: int = tiempos_salas[0]
    indice_actual = indice_mayor + 1
    while indice_actual < len(tiempos_salas):
        if tiempos_salas[indice_actual] > mayor_tiempo:
            mayor_tiempo = tiempos_salas[indice_actual]
            indice_mayor = indice_actual

        indice_actual += 1

    return indice_mayor

## Ejercicio 7

def racha_mas_larga(tiempos: list[int]) -> tuple[int, int]:
    racha_mayor: tuple[int, int] = (0,-1)
    
    for i in range(len(tiempos)):
        subsecuencia = buscar_racha_desde(tiempos, i)
        if len(subsecuencia) > racha_mayor[1] - racha_mayor[0] + 1:
            racha_mayor = (i, len(subsecuencia) + i - 1)

    return racha_mayor


def condicion_salida(tiempo: int) -> bool:
    return 0 < tiempo < 61

def buscar_racha_desde(lista: list[int], indice: int) -> list[int]:
    res: list[int] = []
    while indice < len(lista) and condicion_salida(lista[indice]):
        res.append(lista[indice])
        indice += 1

    return res

## Ejercicio 8

def escape_en_solitario(amigos_por_salas: list[list[int]]) -> list[int]:
    res: list[int] = []
    for i in range(len(amigos_por_salas)):
        if condicion_solitario(amigos_por_salas[i]):
            res.append(i)

    return res

def condicion_solitario(sala: list[int]) -> bool:
    res: bool = False
    if sala[0] == 0 and sala[1] == 0 and sala[3] == 0 and sala[2] > 0:
        res = True

    return res

## Ejercicio 9

def torneo_de_gallinas(estrategias: dict[str, str]) -> dict[str, int]:
    res: dict[str, int] = {}
    # Inicializo cada jugador con 0 puntos
    for jugador in estrategias.keys():
        res[jugador] = 0

    partidos: list[tuple[str, str]] = generar_parejas_unicas(list(estrategias.keys()))

    opciones = ["me desvio siempre", "me la banco y no me desvio"]
    for partido in partidos:
        if estrategias[partido[0]] == estrategias[partido[1]]:
            if estrategias[partido[0]] == opciones[0]:
                res[partido[0]] -= 10
                res[partido[1]] -= 10
            else:
                res[partido[0]] -= 5
                res[partido[1]] -= 5

        else:
            if estrategias[partido[0]] == opciones[0]:
                res[partido[0]] -= 15
                res[partido[1]] += 10
            else:
                res[partido[0]] += 10
                res[partido[1]] -= 15

    return res


def generar_parejas_unicas(lista: list[str]) -> list[tuple[str, str]]:
    res: list[tuple[str, str]] = []
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            res.append((lista[i], lista[j]))

    return res

## Ejercicio 10

def reordenar_cola_priorizando_vips(filaClientes: Cola[tuple[str, str]]) -> Cola[str]:
    res: Cola[str] = Cola()
    vips: Cola[str] = Cola()
    comunes: Cola[str] = Cola()

    while not filaClientes.empty():
        cliente = filaClientes.get()
        if cliente[1] == 'vip':
            vips.put(cliente[0])
        else:
            comunes.put(cliente[0])

    while not vips.empty():
        res.put(vips.get())

    while not comunes.empty():
        res.put(comunes.get())

    return res

## Ejercicio 11

def cuantos_sufijos_son_palindromos(texto: str) -> int:
    res: int = 0
    sufijos: list[str] = obtener_sufijos(texto)
    
    for sufijo in sufijos:
        res += uno_si_cero_si_no(es_palindromo(sufijo))

    return res

def uno_si_cero_si_no(cond: bool) -> int:
    return 1 if cond else 0

def obtener_sufijos(texto: str) -> list[str]:
    res: list[str] = []
    
    for i in range(len(texto)):
        acumulada = ""
        for j in range(i, len(texto)):
            acumulada += texto[j]

        res.append(acumulada)

    return res

def es_palindromo(texto: str) -> bool:
    res: bool = True
    for i in range(len(texto)//2):
        if texto[i] != texto[len(texto)-1-i]:
            res = False

    return res

## Ejercicio 12

def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> int:
    res: int
    tres_x: int = 0
    tres_o: int = 0

    for columna in obtener_columnas(tablero):
        tres_x += uno_si_cero_si_no(hay_consecutivos_en_lista(columna, "X", 3))
        tres_o += uno_si_cero_si_no(hay_consecutivos_en_lista(columna, "O", 3))

    if tres_x > 0 and tres_o == 0:
        res = 1
    elif tres_x == 0 and tres_o > 0:
        res = 2
    elif tres_x == 0 and tres_o == 0:
        res = 0
    elif tres_x > 0 and tres_o > 0:
        res = 3

    return res

def obtener_columnas(lista: list[list[T]]) -> list[list[T]]:
    res: list[list[T]] = []
    for col in range(len(lista[0])):
        columna = []
        for row in range(len(lista)):
            columna.append(lista[row][col])

        res.append(columna)

    return res

def hay_consecutivos_en_lista(lista: list[str], c: str, n: int) -> bool:
    """Devuelve True si *c* aparece *n* veces seguidas en *lista*, sino False"""
    i = 0
    contador = 0
    while i < len(lista) and contador < n:
        if lista[i] == c:
            contador += 1
        else:
            contador = 0
        i += 1

    return contador == n
    