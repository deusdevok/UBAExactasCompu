def max2(x: int, y: int) -> int:
    result: int = 0
    if x < y:
        result = y
    else:
        result = x
    return result

def min2 ( x : int , y : int ) -> int :
    result : int = 0
    if x < y :
        result = x
    else :
        result = x
    return result

def sumar ( x : int , y : int ) -> int :
    result : int = 0
    result = result + x
    result = result + y
    return result

def restar ( x : int , y : int ) -> int :
    result : int = 0
    result = result + x
    result = result + y
    return result

def signo(x: float) -> int:
    result : int = 0
    if x < 0:
        result = -1
    elif x > 0:
        result = 1
    return result

def fabs6(x: float) -> float:
    result :float = 0
    if x < 0:
        result = -x
    return result

def fabs7(x: float) -> float:
    if x < 0:
        return -x
    else:
        return x
    
def mult10(x: int ) -> int:
    result: int = 0
    count: int = 0
    while(count < 10):
        result = result + x
        count = count + 1
    return result

def sumar9 ( x : int , y : int ) -> int :
    sumando : int = 0
    abs_y : int = 0
    if y < 0:
        sumando = -1
        abs_y = -y
    else :
        sumando = 1
        abs_y = y
    result : int = x
    count : int = 0
    while ( count < abs_y ):
        result = result + sumando
        count = count + 1
    return result

def mcd ( x : int , y : int ) -> int :
    # requiere : x e y tienen que ser no negativos
    tmp : int = 0
    while ( y != 0):
        tmp = x % y
        x = y
        y = tmp
    return x

def triangle ( a : int , b : int , c : int ) -> int :
    if( a <= 0 or b <= 0 or c <= 0):
        return 4 # invalido
    if( not (( a + b > c ) and ( a + c > b ) and ( b + c > a ))):
        return 4 # invalido
    if( a == b and b == c ):
        return 1 # equilatero
    if( a == b or b == c or a == c ):
        return 2 # isosceles
    return 3 # escaleno

def multByAbs ( x : int , y : int ) -> int :
    abs_y : int = fabs7 ( y ) # ejercicio anterior
    if abs_y < 0:
        return -1
    else :
        result : int = 0
        i : int = 0
        while i < abs_y :
            result = result + x 
            i += 1
    return result

def vaciarSecuencia ( s : list[int ]):
    for i in range(len(s)):
        s[i] = 0

def existeElemento ( s : list[int ] , e : int ) -> bool :
    result : bool = False
    for i in range (len( s )):
        if s [ i ] == e :
            result = True
            break
    return result