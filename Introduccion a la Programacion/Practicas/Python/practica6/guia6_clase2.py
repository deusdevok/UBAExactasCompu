def volumen_esfera(radio:float) -> float:
    #aproximamos pi a 3,14
    return 4/3 * 3.14 * radio**3


def triada_pitagorica(a: int, b: int, c:int) -> bool:
    return a**2 + b**2 == c*2