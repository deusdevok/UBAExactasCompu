def suma(a: int, b: int) -> int:
    return a+b

def triada_pitagorica(a: int, b: int, c: int) -> bool:
    return a**2 + b**2 == c**2

def es_multiplo_de(n: int, m: int) -> bool:
    return n%m == 0

def devolver_el_doble_si_es_par(numero: int) -> int:
    if numero%2 == 0:
        return 2*numero
    return numero

def fahrenheit_a_celsius(temp_far: float) -> float:
    res: float = (temp_far-32)*5/9
    return res

def es_primo(n: int) -> bool:
    if n < 2:
        return False
    
    for i in range(2, n):
        if n%i == 0:
            return False
        
    return True

def cantidad_primos_en_rango(m: int, n: int) -> int:
    if m > n:
        m, n = n, m

    total = 0
    for i in range(m, n+1):
        if es_primo(i):
            total += 1

    return total