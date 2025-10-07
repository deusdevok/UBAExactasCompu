# def suma2(x:int, y:int) -> int:
#     res: int = x+y
#     return res
#     a = 2
#     print(a)

# print(suma2(2,3))

# for n in range(3):
#     if n == 20:
#         print('hi')
#         break
# else:
#     print('bye')

def duplicar(x: list, y: list):
    y += x # or y = y + x, behaviour is totally different
    y *= 2 # y = y*2

x = [1,2,3]
y = ['a','b','c']

print(f"ANTES: x={x}, y={y}") # x=[1,2,3], y=['a','b','c']
duplicar(x,y)
print(f"DESPUES: x={x}, y={y}") # x=[1,2,3], y=[1,2,3,1,2,3]

# def ejGlobalScope():
#     global x
#     print("x:", x)
#     x = 40
#     print("x:", x)

# def modificarXGlobal():
#     x = x + 20
#     print("x:", x)

# x: int = 20
# ejGlobalScope()
# modificarXGlobal()