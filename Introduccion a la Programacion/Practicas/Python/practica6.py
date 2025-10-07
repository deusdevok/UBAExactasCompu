# Ejercicio 2

import math

def imprimir_saludo(nombre: str):
    print("Hola", nombre)

def raiz_cuadrada_de(numero: float) -> float:
    res: float = math.sqrt(numero)
    return res

def fahrenheit_a_celsius(temp_far: float) -> float:
    res: float = (temp_far-32)*5/9
    return res

def imprimir_dos_veces(estribillo: str):
    print(estribillo*2)

def es_multiplo_de(n: int, m: int) -> bool:
    return n%m == 0

def es_par(numero: int) -> bool:
    res: bool = es_multiplo_de(numero, 2)
    return res

def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    cant_total_porciones: int = comensales * min_cant_de_porciones
    cant_min_pizzas: int = math.ceil(cant_total_porciones / 8)
    return cant_min_pizzas

imprimir_saludo("carlos")
print(raiz_cuadrada_de(9))
print(fahrenheit_a_celsius(80))
imprimir_dos_veces("Esto es algun estribillo de por ahi")
print("25 multiplo de 5?", es_multiplo_de(25, 5))
print("25 multiplo de 4?", es_multiplo_de(25, 4))
print(es_par(88))
print(cantidad_de_pizzas(3, 5)) # 2

# Ejercicio 3

def alguno_es_0(numero1, numero2):
    return numero1 == 0 or numero2 == 0

def ambos_son_0(numero1, numero2):
    return numero1 == 0 and numero2 == 0

def es_nombre_largo(nombre: str) -> bool:
    longitud_nombre = len(nombre)
    return longitud_nombre >= 3 and longitud_nombre <= 8

def es_bisiesto(anio: int) -> bool:
    return anio%400 == 0 or (anio%4 == 0 and anio%100 != 0)

print(alguno_es_0(1, 2)) # False
print(alguno_es_0(1, 0)) # True
print(alguno_es_0(0, 1)) # True
print(alguno_es_0(0, 0)) # True

print(ambos_son_0(1, 2)) # False
print(ambos_son_0(1, 0)) # False
print(ambos_son_0(0, 1)) # False
print(ambos_son_0(0, 0)) # True

# Ejercicio 4

def peso_pino(altura: float) -> float:
    pass

# Ejercicio 5

def devolver_el_doble_si_es_par(numero: int) -> int:
    if numero%2 == 0:
        return 2*numero
    return numero

# Ejercicio 6

def imprimir_pares_entre_10_y_40():
    ind: int = 10
    while ind <= 40:
        print(ind)
        ind += 2

imprimir_pares_entre_10_y_40()

def mostrar_cuenta_regresiva(desde: int):
    while desde >= 1:
        print(desde)
        desde -= 1

    print("Despegue!")

mostrar_cuenta_regresiva(10)