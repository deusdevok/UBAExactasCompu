import unittest
from p10 import *

class TestVeterinariaStock(unittest.TestCase):
    def test_stock_vacio(self):
        self.assertEqual(stock_productos([]), {})

    def test_stock_unico_producto(self):
        self.assertEqual(stock_productos([("comida", 3)]), {"comida": (3,3)})

    def test_stock_min(self):
        self.assertEqual(stock_productos([("comida", 3), ("huesito", 0), ("mantita", 5), ("comida", 1)]), {"comida": (1,3), "huesito": (0,0), "mantita": (5,5)})

    def test_stock_max(self):
        self.assertEqual(stock_productos([("comida", 3), ("huesito", 0), ("mantita", 5), ("comida", 5)]), {"comida": (3,5), "huesito": (0,0), "mantita": (5,5)})

    def test_stock_eq(self):
        self.assertEqual(stock_productos([("comida", 3), ("comida", 3)]), {"comida": (3,3)})

class TestFiltrarCodigosPrimos(unittest.TestCase):
    def test_codigos_primos_vacio(self):
        self.assertEqual(filtrar_codigos_primos([]), [])

    def test_codigos_primos_mix(self):
        self.assertEqual(filtrar_codigos_primos([3123002, 634, 4681384101, 8461394107]), [3123002, 4681384101, 8461394107])

class TestSubsecuenciaMasLarga(unittest.TestCase):
    def test_sub_mas_larga_unico_elemento(self):
        self.assertEqual(subsecuencia_mas_larga(["perro"]), 0)

    def test_sub_mas_larga_todos_perro(self):
        self.assertEqual(subsecuencia_mas_larga(["perro","perro","perro"]), 0)

    def test_sub_mas_larga_todos_gato(self):
        self.assertEqual(subsecuencia_mas_larga(["gato","gato","gato"]), 0)

    def test_sub_mas_larga_todos_perro_gato(self):
        self.assertEqual(subsecuencia_mas_larga(["gato","perro","gato"]), 0)

    def test_sub_mas_larga_repetidas(self):
        self.assertEqual(subsecuencia_mas_larga(["gato","pato","gato","perro","rata","perro","gato","pollo","oruga"]), 2)

class TestTablaTurnos(unittest.TestCase):
    def test_tabla_turnos(self):
        tabla = [
            ["carlos","lucas","romina"],
            ["carlos","jorge","andrea"],
            ["carlos","jorge","andrea"],
            ["carlos","jorge","andrea"],
            ["pepe","david","stella"],
            ["pepe","david","ariel"],
            ["pepe","david","ariel"],
            ["pepe","david","ariel"],
        ]
        self.assertEqual(un_responsable_por_turno(tabla), [(True,True),(False,True),(False,False)])

class TestSalaEscapePromedios(unittest.TestCase):
    def test_sala_vacia(self):
        self.assertEqual(promedio_de_salidas({}), {})

    def test_sala_unico_elemento(self):
        registro = {"carlos": [2]}
        self.assertEqual(promedio_de_salidas(registro), {"carlos": (1, 2)})

    def test_sala_todos_invalidos(self):
        registro = {"carlos": [0,0,61], "pepe": [0,61,0]}
        self.assertEqual(promedio_de_salidas(registro), {"carlos": (0,0), "pepe": (0,0)})

    def test_sala_algunos_salieron(self):
        registro = {"carlos": [0,45,61], "pepe": [48,61,55]}
        esperado = {"carlos": (1,45), "pepe": (2, 51.5)}
        self.assertEqual(promedio_de_salidas(registro), esperado)

if __name__ == "__main__":
    unittest.main()