"""
En este archivo quiero practicar abrir archivos, paths, etc
"""

import os

nombre_archivo = "himno_argentino.txt"

# Imprime el path al archivo py que estoy ejecutando
# __file__ pareceria ser un objeto con informacion del archivo actual
print(__file__)
print("type de __file__:", type(__file__)) # Es de tipo string...

# Usando paths
p = os.path.abspath(__file__)
print(p)
print(f"Tipo de abspath:", type(p))
# Un comentario al final (prueba)# Un comentario al final (prueba)# Un comentario al final (prueba)
# Un comentario al final (prueba)
# Un comentario al final (prueba)
# Un comentario al final (prueba)
# Un comentario al final (prueba)
# Un comentario al final (prueba)
# Un comentario al final (prueba)
# Un comentario al final (prueba)
