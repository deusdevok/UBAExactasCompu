# Un comentario al principio (prueba)
# Un comentario al principio (prueba)
"""
En este archivo quiero practicar abrir archivos, paths, etc
"""

import os

nombre_archivo = "himno_argentino.txt"

print(__file__)
print("type de __file__:", type(__file__)) # Es de tipo string...

p = os.path.abspath(__file__)
print(p)
print(f"Tipo de abspath:", type(p))