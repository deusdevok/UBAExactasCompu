## Ejercicio 16

def calcular_promedio_por_estudiante(notas: list[tuple[str, float]]) -> dict[str, float]:
    d: dict[str, list[float]] = {}
    for nota in notas:
        if nota[0] not in d:
            d[nota[0]] = [nota[1]]
        else:
            d[nota[0]].append(nota[1])

    d_final: dict[str, float] = {}
    for k, v in d.items():
        d_final[k] = sum(v)/len(v)

    return d_final

# notas: list[tuple[str, float]] = [("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]
# print(calcular_promedio_por_estudiante(notas))

## Ejercicio 17
from queue import LifoQueue as Pila

def visitar_sitio(historiales: dict[str, Pila[str]], usuario: str, sitio: str):
    if usuario not in historiales:
        historiales[usuario] = Pila()
    
    historiales[usuario].put(sitio)

historiales: dict[str, Pila[str]] = {
    "carlos": Pila(),
    "pepe": Pila(),
    "maria": Pila()
}

# visitar_sitio(historiales, "carlos", "AED-I")
# visitar_sitio(historiales, "carlos", "AED-II")
# print(historiales["carlos"].get())
# print(historiales["carlos"].get())

def navegar_atras(historiales: dict[str, Pila[str]], usuario: str) -> str:
    return historiales[usuario].get()

# historiales = {}
# visitar_sitio(historiales, "Usuario1", "google.com")
# visitar_sitio(historiales, "Usuario1", "facebook.com")
# print(navegar_atras(historiales, "Usuario1"))
# visitar_sitio(historiales, "Usuario2", "youtube.com")

## Ejercicio 18

def agregar_producto(inventario: dict[str, dict[str, float | int]], nombre: str, precio: float, cantidad: int):
    inventario[nombre] = {"precio": precio, "cantidad": cantidad}

def actualizar_stock(inventario: dict[str, dict[str, float | int]], nombre: str, cantidad: int):
    inventario[nombre]["cantidad"] = cantidad

def actualizar_precio(inventario: dict[str, dict[str, float | int]], nombre: str, precio: float):
    inventario[nombre]["precio"] = precio

def calcular_valor_inventario(inventario: dict[str, dict[str, float | int]]) -> float:
    total: float = 0
    for nombre, info in inventario.items():
        total += info["precio"] * info["cantidad"]

    return total

inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalon", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total) # Deberia imprimir 1100.0