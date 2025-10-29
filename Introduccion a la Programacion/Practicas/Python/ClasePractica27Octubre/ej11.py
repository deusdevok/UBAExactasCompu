def triangle(a: int, b: int, c: int) -> int:
    if (a <= 0 or b <= 0 or c <= 0):
        return 4
    if (not ((a+b > c) and (a+c > b) and (b+c > a))):
        return 4
    if (a == b and b == c):
        return 1
    if (a == b or b == c or a == c):
        return 2
    return 3