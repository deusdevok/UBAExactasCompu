def imprimir_hola_mundo():
    hola: str = "Hola mundo!"
    print(hola)

imprimir_hola_mundo()

def imprimir_un_verso():
    print("la cucaracha, la cucaracha,")
    print("ya no puede caminar,")
    print("porque no tiene, porque le faltan,")
    print("las dos patitas de atras")

imprimir_un_verso()

import math

def raizDe2() -> float:
    raiz: float = math.sqrt(2)
    raiz_redondeada: float = round(raiz, 4)
    return raiz_redondeada

print("Raiz de 2 =", raizDe2())

def factorial_de_dos() -> int:
    res: int = 2*1
    return res

print("Factorial de 2 =", factorial_de_dos())

def perimetro() -> float:
    perimetro: float = 2*math.pi
    return perimetro

print("Perimetro de circunferencia de radio 1 =", perimetro())