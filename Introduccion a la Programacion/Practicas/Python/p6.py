# Ejercicio 1

def imprimir_hola_mundo():
    hola: str = "Hola mundo!"
    print(hola)

# imprimir_hola_mundo()

def imprimir_un_verso():
    # Podria usarse \n en vez de varios print para separar
    print("la cucaracha, la cucaracha,")
    print("ya no puede caminar,")
    print("porque no tiene, porque le faltan,")
    print("las dos patitas de atras")

# imprimir_un_verso()

import math

def raizDe2() -> float:
    raiz: float = math.sqrt(2)
    raiz_redondeada: float = round(raiz, 4)
    return raiz_redondeada

# print("Raiz de 2 =", raizDe2())

def factorial_de_dos() -> int:
    res: int = 2*1
    return res

# print("Factorial de 2 =", factorial_de_dos())

def perimetro() -> float:
    perimetro: float = 2*math.pi
    return perimetro

# print("Perimetro de circunferencia de radio 1 =", perimetro())

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

# imprimir_saludo("carlos")
# print(raiz_cuadrada_de(9))
# print(fahrenheit_a_celsius(80))
# imprimir_dos_veces("Esto es algun estribillo de por ahi")
# print("25 multiplo de 5?", es_multiplo_de(25, 5))
# print("25 multiplo de 4?", es_multiplo_de(25, 4))
# print(es_par(88))
# print(cantidad_de_pizzas(3, 5)) # 2

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

# print(alguno_es_0(1, 2)) # False
# print(alguno_es_0(1, 0)) # True
# print(alguno_es_0(0, 1)) # True
# print(alguno_es_0(0, 0)) # True

# print(ambos_son_0(1, 2)) # False
# print(ambos_son_0(1, 0)) # False
# print(ambos_son_0(0, 1)) # False
# print(ambos_son_0(0, 0)) # True

# Ejercicio 4

def peso_pino(altura: float) -> float:
    """
    Calcula el peso de un pino segun su altura

    altura en metros
    devuelve peso en Kg
    """
    peso: float
    if altura <= 3:
        peso = altura*100*3
    else:
        peso = 3*100*3 + (altura-3)*100*2

    return peso

def es_peso_util(peso: float) -> bool:
    return 400 <= peso <= 1000

def sirve_pino(altura: float) -> bool:
    return es_peso_util(peso_pino(altura))


# Ejercicio 5

def devolver_el_doble_si_es_par(numero: int) -> int:
    return 2*numero if es_par(numero) else numero

def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    return numero if es_par(numero) else numero+1

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if es_multiplo_de(numero, 9):
        return numero*3
    elif es_multiplo_de(numero, 3):
        return numero*2
    else:
        return numero
    
def lindo_nombre(nombre: str) -> str:
    if len(lindo_nombre) >= 5:
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"
    
def elRango(numero: int):
    if numero < 5:
        print("Menor a 5")
    elif 10 <= numero <= 20:
        print("Entre 10 y 20")
    elif numero > 20:
        print("Mayor a 20")
    else:
        print("Numero en rango desconocido")

def trabajar_o_vacacionar(sexo: str, edad: int):
    jubilado = (edad >= 60 and sexo == "F") or (edad >= 65 and sexo == "M")
    menor = edad < 18

    if jubilado or menor:
        print("Anda de vacaciones")
    else:
        print("Te toca trabajar")


# Ejercicio 6

def imprimir_del_1_al_10():
    numero: int = 1
    while numero <= 10:
        print(numero)
        numero += 1

def imprimir_pares_entre_10_y_40():
    ind: int = 10
    while ind <= 40:
        print(ind)
        ind += 2

# imprimir_pares_entre_10_y_40()

def imprimir_eco_10_veces():
    contador: int = 1
    while contador <= 10:
        print("eco")
        contador += 1

def mostrar_cuenta_regresiva(desde: int):
    while desde >= 1:
        print(desde)
        desde -= 1

    print("Despegue!")

# mostrar_cuenta_regresiva(10)

def viaje_en_el_tiempo(partida: int, llegada: int):
    while partida > llegada:
        partida -= 1
        print(f"Viajo un anio al pasado. Estamos en el anio {partida}")

# viaje_en_el_tiempo(2025, 1990)

def viaje_en_el_tiempo_rapido(partida: int, llegada: int):
    while partida > llegada:
        partida -= 20
        print(f"Viajo 20 anio al pasado. Estamos en el anio {partida}")

# viaje_en_el_tiempo_rapido(2025, -384)

# Ejercicio 7

def imprimir_del_1_al_10_for():
    for i in range(1, 11):
        print(i)

# imprimir_del_1_al_10_for()

def imprimir_pares_entre_10_y_40_for():
    for i in range(10, 41, 2):
        print(i)

# imprimir_pares_entre_10_y_40_for()

def imprimir_eco_10_veces_for():
    for _ in range(10):
        print("eco")

# imprimir_eco_10_veces_for()

def mostrar_cuenta_regresiva_for(desde: int):
    for i in range(desde, 0, -1):
        print(i)

    print("Despegue!")

# mostrar_cuenta_regresiva_for(3)

def viaje_en_el_tiempo_for(partida: int, llegada: int):
    for anio in range(partida-1, llegada-1, -1):
        print(f"Viajo un anio al pasado. Estamos en el anio {anio}")

# viaje_en_el_tiempo_for(2025, 2001)

def viaje_en_el_tiempo_rapido_for(partida: int, llegada: int):
    for anio in range(partida-20, llegada-1, -20):
        print(f"Viajo 20 anio al pasado. Estamos en el anio {anio}")

# viaje_en_el_tiempo_rapido_for(2025, -384)

# Ejercicio 8

"""
1. 
x=5
# Estado a: x == 5
y=7
# Estado b: y == 7, x == 5
x = x + y
# Estado c: x == x@b + y@b == 12

2. 
x=5
# Estado a: x == 5
y=7
# Estado b: y == 7, x == 5
z=x+y
# Estado c: z == x@b+y@b == 12
y = z * 2
# Estado d: y == z@c*2 == 24


3. x=5 ; y=7 ; x="hora"; y = x * 2
4. x=False ; res=not(x)
5. x=False ; x=not(x)
6. x=True ; y=False ; res=x and y; x = res and x
"""

# Ejercicio 9

"""
problema rt (in x: int, in g: int): int {
    asegura: {res es la suma de x, g y 1}
}
"""
def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0

"""
problema ro (x: int): int {
    modifica: {variable global g}
    asegura: {res es ka syna de x, g y 1}
}
"""
def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g

# 1)
# # g == 0
# print(ro(1)) # devuelve 1+(0+1)=2
# # g == 1

# # g == 1
# print(ro(1)) # devuelve 1+(1+1)=3
# # g == 2

# # g == 2
# print(ro(1)) # devuelve 1+(2+1)=4
# # g == 3

# 2)

print(rt(1, 0)) # devuelve 2

print(rt(1, 0)) # devuelve 2

print(rt(1, 0)) # devuelve 2