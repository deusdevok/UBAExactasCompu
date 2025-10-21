from queue import LifoQueue as Pila, Queue as Cola
from random import randint, shuffle, sample
from typing import TypeVar


T = TypeVar('T')

######################
## PILAS
####################

## Ejercicio 1

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila:
    p: Pila[int] = Pila()
    for _ in range(cantidad):
        rnd = randint(desde, hasta)
        p.put(rnd)

    return p

# p = generar_nros_al_azar(12, 1, 10)
# mostrar_pila_completa(p)
# print(p.get())

## Ejercicio 2

def cantidad_elementos(p: Pila) -> int:
    # El parametro p es in, asi que no tiene que modificarse al terminar
    tamanio: int = 0
    p_aux: Pila = Pila()
    while not p.empty():
        e = p.get()
        tamanio += 1
        p_aux.put(e)

    # Revierto la pila original
    while not p_aux.empty():
        p.put(p_aux.get())

    return tamanio

# p = Pila()
# p.put(1)
# p.put(2)
# p.put(3)
# p.put(4)
# print(cantidad_elementos(p))

# print(p.empty())


## Ejercicio 3

def buscar_el_maximo(p: Pila) -> int:
    pila_aux: Pila[int] = Pila()
    maximo_hasta_ahora: int = p.get()

    pila_aux.put(maximo_hasta_ahora)
    while not p.empty():
        aux = p.get()
        pila_aux.put(aux)
        maximo_hasta_ahora = max(maximo_hasta_ahora, aux)

    # Revierto la pila original, que ahora quedo vacia
    while not pila_aux.empty():
        p.put(pila_aux.get())

    return maximo_hasta_ahora

# p = Pila()
# p.put(2)
# p.put(9)
# p.put(12)
# p.put(3)

# print(buscar_el_maximo(p))

# print("Pila vacia?", p.empty(), p.get())

## Ejercicio 4

def buscar_nota_maxima(p: Pila[tuple[str, int]]) -> tuple[str, int]:
    p_aux = Pila()
    n = p.get()
    p_aux.put(n)
    maximo_hasta_ahora: tuple[str, int] = n

    while not p.empty():
        n = p.get()
        if n[1] > maximo_hasta_ahora[1]:
            maximo_hasta_ahora = n

        p_aux.put(n)

    # Vuelvo a reconstruir p
    while not p_aux.empty():
        p.put(p_aux.get())

    return maximo_hasta_ahora

# p = Pila()
# p.put(("Fisica", 8))
# p.put(("Fisica", 6))
# p.put(("Fisica", 10))
# p.put(("Fisica", 2))

# print(buscar_nota_maxima(p))
# print(p.empty())

## Ejercicio 5

def espiar_pila(p: Pila[T]) -> T:
    # Devuelve el elemento de arriba y mantiene la pila intacta
    # Requiere que p no este vacia (si esta vacia puede dar error)
    n = p.get()
    p.put(n)
    return n

def esta_bien_balanceada(s: str) -> bool:
    p: Pila = Pila()

    for c in s:
        if c == '(' or c == ')':
            if p.empty():
                p.put(c)
            else:
                top = espiar_pila(p)
                if top == '(' and c == ')':
                    p.get()
                else:
                    p.put(c)

    return p.empty()

# print("TRUE", esta_bien_balanceada("()"))
# print("TRUE", esta_bien_balanceada("1 + ( 2 x 3 = ( 2 0 / 5 ) )"))
# print("TRUE", esta_bien_balanceada("10 * ( 1 + ( 2 * ( =1)))"))
# print("FALSE", esta_bien_balanceada("1 + ) 2 x 3 ( ( )"))

## Ejercicio 6

def evaluar_expresion(s: str) -> float:
    tokens: list[str] = []
    for c in s:
        if c != ' ':
            tokens.append(c)

    p = Pila()
    for token in tokens:
        if token not in "+-*/":
            p.put(token)
        else:
            ultimo = float(p.get())
            anteultimo = float(p.get())
            if token == "+":
                p.put(anteultimo + ultimo)
            elif token == "-":
                p.put(anteultimo - ultimo)
            elif token == "*":
                p.put(anteultimo * ultimo)
            elif token == "/":
                p.put(anteultimo / ultimo)

    return p.get()

# print(evaluar_expresion("3 4 + 5 * 2 -"))
# print(evaluar_expresion("3 4 -"))
# print(evaluar_expresion("3 4 /"))

## Ejercicio 7

def intercalar(p1: Pila, p2: Pila) -> Pila:
    p_intercalada: Pila = Pila()
    p_intercalada_aux: Pila = Pila()
    while not p1.empty():
        p_intercalada_aux.put(p2.get())
        p_intercalada_aux.put(p1.get())

    while not p_intercalada_aux.empty():
        n1 = p_intercalada_aux.get()
        p_intercalada.put(n1)
        p1.put(n1)

        n2 = p_intercalada_aux.get()
        p_intercalada.put(n2)
        p2.put(n2)

    return p_intercalada

# p1 = Pila()
# p2 = Pila()
# p1.put(3)
# p1.put(2)
# p1.put(1)
# p2.put(5)
# p2.put(6)
# p2.put(7)
# p_inter = intercalar(p1,p2)
# print(p_inter.get())
# print(p_inter.get())
# print(p_inter.get())
# print(p_inter.get())
# print(p_inter.get())
# print(p_inter.get())

# print("p1 top:", p1.get())
# print("p2 top:", p2.get())

################
## COLAS
###############


## Ejercicio 8

def generar_nros_al_azar_cola(cantidad: int, desde: int, hasta: int) -> Cola:
    q: Cola = Cola()
    for _ in range(cantidad):
        nro = randint(desde, hasta)
        q.put(nro)
    
    return q

# q = generar_nros_al_azar_cola(8, 10, 100)
# print(q.qsize())
# print(q.get())

## Ejercicio 9

def cantidad_elementos_cola(c: Cola) -> int:
    total: int = 0
    cola_aux: Cola = Cola()
    while not c.empty():
        cola_aux.put(c.get())
        total += 1

    while not cola_aux.empty():
        c.put(cola_aux.get())

    return total

# c = Cola()
# c.put(1)
# c.put(2)
# c.put(3)
# c.put(4)

# print(cantidad_elementos_cola(c))
# print(c.get())

## Ejercicio 10

def buscar_el_maximo_cola(c: Cola) -> int:
    cola_aux: Cola = Cola()
    max_hasta_ahora: int = c.get()
    cola_aux.put(max_hasta_ahora)
    while not c.empty():
        n = c.get()
        max_hasta_ahora = max(max_hasta_ahora, n)
        cola_aux.put(n)

    # Reconstruyo cola original
    while not cola_aux.empty():
        c.put(cola_aux.get())

    return max_hasta_ahora

# c = Cola()
# c.put(1)
# c.put(1)
# c.put(10)
# c.put(2)

# print(buscar_el_maximo_cola(c))
# print(c.get())

# La implementacion es la misma que con pila, pero usando cola

## Ejercicio 11

def buscar_nota_minima_cola(c: Cola[(str, int)]) -> tuple[str, int]:
    cola_aux: Cola = Cola()
    minimo_hasta_ahora: tuple[str, int] = c.get()
    cola_aux.put(minimo_hasta_ahora)
    while not c.empty():
        elem = c.get()
        if elem[1] < minimo_hasta_ahora[1]:
            minimo_hasta_ahora = elem

        cola_aux.put(elem)

    # Reconstruyo cola original
    while not cola_aux.empty():
        c.put(cola_aux.get())

    return minimo_hasta_ahora

# c = Cola()
# c.put(("Mate", 5))
# c.put(("Fisica", 2))
# c.put(("Algo 1", 10))
# c.put(("Algo 2", 8))

# print(buscar_nota_minima_cola(c))
# print(c.get())

## Ejercicio 12

def intercalar_cola(c1: Cola, c2: Cola) -> Cola:
    cola_nueva: Cola = Cola()
    c1_aux = Cola()
    c2_aux = Cola()

    while not c1.empty():
        n1 = c1.get()
        cola_nueva.put(n1)
        n2 = c2.get()
        cola_nueva.put(n2)

        c1_aux.put(n1)
        c2_aux.put(n2)

    while not c1_aux.empty():
        c1.put(c1_aux.get())
        c2.put(c2_aux.get())

    return cola_nueva

# c1 = Cola()
# c1.put(1)
# c1.put(2)
# c1.put(3)
# c2 = Cola()
# c2.put(10)
# c2.put(20)
# c2.put(30)

# c = intercalar_cola(c1, c2)
# print(c.get())
# print(c.get())
# print(c.get())
# print(c.get())
# print(c.get())
# print(c.get())

# print(c1.get())
# print(c2.get())

## Ejercicio 13

def armar_secuencia_de_bingo() -> Cola[int]:
    q: Cola[int] = Cola()
    numeros_mezclados: list[int] = list(range(100))
    shuffle(numeros_mezclados)
    
    for n in numeros_mezclados:
        q.put(n)

    return q

# q = armar_secuencia_de_bingo()
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas: int = 0
    numeros_restantes: int = 12
    bolillero_aux = Cola()

    while numeros_restantes > 0:
        numero = bolillero.get()
        if numero in carton:
            numeros_restantes -= 1
        
        jugadas += 1
        bolillero_aux.put(numero)

    # Reconstruyo bolillero
    while not bolillero_aux.empty():
        bolillero.put(bolillero_aux.get())

    return jugadas

# cantidad_total_numeros = 100
# numeros_en_carton = 12
# bolillas: Cola = armar_secuencia_de_bingo()
# carton: list[int] = sample(range(cantidad_total_numeros), numeros_en_carton)
# print(jugar_carton_de_bingo(carton, bolillas))
# print(carton)
# print(bolillas.get())
# print(bolillas.get())
# print(bolillas.get())

## Ejercicio 14

def pacientes_urgentes(c: Cola[(int, str, str)]) -> int:
    cantidad_urgentes: int = 0
    c_aux: Cola = Cola()

    while not c.empty():
        elem = c.get()
        prioridad, nombre, especialidad = elem
        if prioridad < 4:
            cantidad_urgentes += 1

        c_aux.put(elem)

    # Reconstruyo cola original
    while not c_aux.empty():
        c.put(c_aux.get())

    return cantidad_urgentes

# pacientes: Cola = Cola()
# pacientes.put((3, "Carlos", "Dentista"))
# pacientes.put((1, "Andrea", "Dentista"))
# pacientes.put((8, "Eloy", "General"))
# pacientes.put((2, "Carlos", "General"))
# pacientes.put((1, "Carlos", "Seguimiento"))
# pacientes.put((7, "Carlos", "Seguimiento"))

# print(pacientes_urgentes(pacientes))
# print(pacientes.get())
# print(pacientes.get())
# print(pacientes.get())
# print(pacientes.get())

## Ejercicio 15

"""
Especificacion

problema atencion_a_clientes (in c: Cola[tuple[str, int, bool, bool]]): Cola[tuple[str, int, bool, bool]] {
    requiere: {La segunda componente de los elementos de c son unicas (DNI)}
    asegura: {res es una cola ordenada por prioridad (cuarta componente), tipo de cuenta (tercer componente), luego el resto}
    asegura: {el orden en cada subgrupo se mantiene}
}
"""

def atencion_a_clientes(c: Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    prioritarios: Cola = Cola()
    preferenciales: Cola = Cola()
    resto: Cola = Cola()

    c_aux: Cola = Cola()

    while not c.empty():
        elem = c.get()
        if elem[3]:
            prioritarios.put(elem)
        elif elem[2]:
            preferenciales.put(elem)
        else:
            resto.put(elem)

        c_aux.put(elem)

    # Junto todos en una misma cola
    cola_final: Cola = Cola()
    
    while not prioritarios.empty():
        cola_final.put(prioritarios.get())

    while not preferenciales.empty():
        cola_final.put(preferenciales.get())

    while not resto.empty():
        cola_final.put(resto.get())

    # Reconstruyo cola original
    while not c_aux.empty():
        c.put(c_aux.get())

    return cola_final

# c: Cola = Cola()
# # Nombre, DNI, tipo cuenta (true: preferencial), prioridad
# c.put(("Carlos", 32777777, True, False))
# c.put(("Pepe", 31777777, True, True))
# c.put(("Roberto", 32774177, True, False))
# c.put(("Lucia", 37677777, False, False))
# c.put(("Maria", 32777117, True, True))
# c.put(("Juan", 32777716, False, True))
# c.put(("Gloria", 32333777, False, False))

# # Orden esperado: Pepe, Maria, Juan, Carlos, Roberto, Lucia, Gloria

# cola_final = atencion_a_clientes(c)
# print(cola_final.get())
# print(cola_final.get())
# print(cola_final.get())
# print(cola_final.get())
# print(cola_final.get())
# print(cola_final.get())
# print(cola_final.get())