import os

def construir_path(nombre_archivo: str):
    script_path = os.path.abspath(__file__)
    cwd = os.path.dirname(script_path)
    archivo_path = os.path.join(cwd, nombre_archivo)

    return archivo_path

## Ejercicio 19

def contar_lineas(nombre_archivo: str) -> int:
    f = open(nombre_archivo, "r")
    lineas: list[str] = f.readlines() # Ineficiente en memoria. Se podria usar for linea in f e ir contando
    f.close()
    return len(lineas)

def existe_palabra(nombre_archivo: str, palabra: str) -> bool:
    f = open(nombre_archivo, "r")
    existe: bool = False
    for linea in f:
        if palabra in linea:
            existe = True

    f.close()

    return existe

def cantidad_de_apariciones(nombre_archivo: str, palabra: str) -> int:
    f = open(nombre_archivo, "r")
    cant_apariciones: int = 0
    for linea in f:
        cant_apariciones += linea.count(palabra)

    f.close()

    return cant_apariciones

# archivo_nombre: str = "himno_argentino.txt"
# script_path = os.path.abspath(__file__)
# cwd = os.path.dirname(script_path)
# archivo_path = os.path.join(cwd, archivo_nombre)

# cantidad_lineas: int = contar_lineas(archivo_path)
# print("Cantidad de lineas del himno Argentino:", cantidad_lineas)
# print("laureles existe?", existe_palabra(archivo_path, "laureles"))
# print("pinocho existe?", existe_palabra(archivo_path, "pinocho"))
# cantidad_apariciones_libertad: int = cantidad_de_apariciones(archivo_path, "libertad")
# print("La palabra libertad aparece", cantidad_apariciones_libertad, " vez (veces) en el himno Argentino")

## Ejercicio 20

def limpiar_puntuacion(s: str) -> str:
    puntuacion: str = """.,;:""“”''‘’¡!¿?()[]{}><\n"""
    limpio: str = ""
    for c in s:
        if c not in puntuacion:
            limpio += c

    return limpio

def agrupar_por_longitud(nombre_archivo: str) -> dict[int, int]:
    f = open(nombre_archivo, "r", encoding="UTF-8")
    d = {}
    for linea in f:
        for palabra in linea.split():
            palabra_limpia = limpiar_puntuacion(palabra)
            if palabra_limpia not in d:
                d[palabra_limpia] = 1
            else:
                d[palabra_limpia] += 1

    f.close()
    return d

# nombre_archivo = "himno_argentino.txt"
# script_path = os.path.abspath(__file__)
# cwd = os.path.dirname(script_path)
# archivo_path = os.path.join(cwd, nombre_archivo)

# d = agrupar_por_longitud(archivo_path)
# print(d)

## Ejercicio 21

def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    d = agrupar_por_longitud(nombre_archivo)

    # Busco el valor maximo en el diccionario
    max_hasta_ahora = 0
    res = ""
    for k, v in d.items():
        if v > max_hasta_ahora:
            max_hasta_ahora = v
            res = k

    return res

# nombre_archivo = "himno_argentino.txt"
# archivo_path = construir_path(nombre_archivo)
# print(f"La palabra mas frecuente en el himno Argentino es: {la_palabra_mas_frecuente(archivo_path)}")

## Ejercicio 22

def clonar_sin_comentarios(nombre_archivo_entrada: str, nombre_archivo_salida: str):
    f_entrada = open(nombre_archivo_entrada, "r", encoding="UTF-8")
    f_salida = open(nombre_archivo_salida, "w", encoding="UTF-8")

    for linea in f_entrada:
        linea_sin_espacios = linea.split()
        if len(linea_sin_espacios) == 0 or linea_sin_espacios[0] != "#":
            f_salida.write(linea)

    f_entrada.close()
    f_salida.close()

# clonar_sin_comentarios(construir_path("archivos_practica.py"), construir_path("archivos_practica_sin_comments.py"))

## Ejercicio 23

from queue import LifoQueue as Pila

def invertir_lineas(nombre_archivo_entrada: str, nombre_archivo_salida: str):
    f_entrada = open(nombre_archivo_entrada, "r", encoding="UTF-8")

    # Uso pila para que quede el orden deseado
    pila: Pila = Pila()
    for linea in f_entrada:
        pila.put(linea)

    f_entrada.close()

    f_salida = open(nombre_archivo_salida, "w", encoding="UTF-8")
    while not pila.empty():
        f_salida.write(pila.get())
    
    f_salida.close()

# invertir_lineas(construir_path("archivos_practica.py"), construir_path("archivos_practica_al_reves.py"))

## Ejercicio 24

def agregar_frase_al_final(nombre_archivo: str, frase: str):
    archivo_entrada = open(nombre_archivo, "a", encoding="UTF-8")
    archivo_entrada.write(frase + "\n")
    archivo_entrada.close()

# agregar_frase_al_final(construir_path("archivos_practica.py"), "# Un comentario al final (prueba)")

## Ejercicio 25

def agregar_frase_al_principio(nombre_archivo: str, frase: str):
    archivo_entrada = open(nombre_archivo, "r+", encoding="UTF-8")
    
    todas_las_lineas = archivo_entrada.readlines()
    todas_las_lineas = [frase + "\n"] + todas_las_lineas

    archivo_entrada.seek(0) # Vuelvo el puntero al principio

    for linea in todas_las_lineas:
        archivo_entrada.write(linea)

    archivo_entrada.close()

# agregar_frase_al_principio(construir_path("archivos_practica_sin_comments.py"), "# Un comentario al principio (prueba)")

def es_texto_legible(s: str) -> bool:
    for c in s:
        if not ("A" <= c <= "Z" or "a" <= c <= "z" or "0" <= c <= "9" or c == " " or c == "_"):
            return False
        
    return len(s) >= 5

def listar_textos_de_archivo(nombre_archivo: str) -> list[str]:
    res: list[str] = []

    f = open(nombre_archivo, "rb")
    contenido = f.read() # Lee el contenido completo del archivo
    
    secuencia_bytes = contenido.split()
    for byte in secuencia_bytes:
        palabra = ""
        for b in byte:
            palabra += chr(b)
        
        if es_texto_legible(palabra):
            res.append(palabra)
    f.close()

    return res


# r = listar_textos_de_archivo(construir_path("himno_argentino.txt"))
# r = listar_textos_de_archivo(construir_path(r"C:\Users\carlos\AppData\Local\DBeaver\dbeaver.exe"))
# r = listar_textos_de_archivo(construir_path(r"C:\Users\carlos\Downloads\closeup-shot-glass-coffee-beans-dark-surface.jpg"))
# print(r)

## Ejercicio 27

def calcular_promedio_por_estudiante(nombre_archivo_notas: str, nombre_archivo_promedios: str):
    notas_csv = open(nombre_archivo_notas, "r", encoding="UTF-8")
    d: dict[str, list[float]] = {}
    for linea in notas_csv:
        lu, materia, fecha, nota = linea.split(sep=',')
        if lu not in d:
            d[lu] = [float(nota)]
        else:
            d[lu].append(float(nota))

    notas_csv.close()

    promedios_csv = open(nombre_archivo_promedios, "w", encoding="UTF-8")
    for lu, notas in d.items():
        promedio_nota = sum(notas)/len(notas)
        linea = f"{lu},{promedio_nota:.2f}\n"
        promedios_csv.write(linea)

    promedios_csv.close()

calcular_promedio_por_estudiante(construir_path("notas_alumnos.csv"), construir_path("notas_alumnos_promedios.csv"))