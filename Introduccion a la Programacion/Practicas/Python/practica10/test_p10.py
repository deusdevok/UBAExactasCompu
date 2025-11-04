from queue import Queue as Cola
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

class TestSalaEscapeTiempoMasRapido(unittest.TestCase):
    def test_unico_tiempo(self):
        self.assertEqual(tiempo_mas_rapido([5]), 0)

    def test_todos_iguales(self):
        self.assertEqual(tiempo_mas_rapido([3,3,3]), 0)

    def test_unico_mayor(self):
        self.assertEqual(tiempo_mas_rapido([1,4,6,3,2]), 2)

    def test_mayor_al_final(self):
        self.assertEqual(tiempo_mas_rapido([5,5,6,9]), 3)

class TestRachaMasLarga(unittest.TestCase):
    def test_racha_minima(self):
        self.assertEqual(racha_mas_larga([20]), (0,0))

    def test_racha_minima_en_el_medio(self):
        self.assertEqual(racha_mas_larga([0,0,61,30,0,0,40]), (3,3))

    def test_racha_en_el_medio(self):
        self.assertEqual(racha_mas_larga([0,61,5,6,7,4,61,0]), (2,5))

    def test_racha_en_el_medio_repetida(self):
        self.assertEqual(racha_mas_larga([0,61,5,6,7,4,61,0, 20,30,40,50,61]), (2,5))

class TestEscapeEnSolitario(unittest.TestCase):
    def test_una_sala(self):
        salas = [[0,0,40,0]]
        self.assertEqual(escape_en_solitario(salas), [0])

    def test_una_sala_no_fue_nadie(self):
        salas = [[0,0,0,0]]
        self.assertEqual(escape_en_solitario(salas), [])

    def test_dos_salas_una_y_una(self):
        salas = [[0,0,0,0],[0,0,61,0]]
        self.assertEqual(escape_en_solitario(salas), [1])

    def test_varias_salas_mix(self):
        salas = [
            [0,0,0,0],
            [0,0,61,0],
            [0,0,40,0],
            [2,2,3,1],
            [0,0,30,0],
            [0,0,30,0],
            [0,0,0,0]
            ]
        self.assertEqual(escape_en_solitario(salas), [1,2,4,5])

class TorneoDeGallinasTest(unittest.TestCase):
    def test_dos_jugadores(self):
        estrategias = {
            "carlos": "me la banco y no me desvio",
            "pablo": "me desvio siempre"
            }
        
        salida_esperada = {
            "carlos": 10,
            "pablo": -15
        }
        
        self.assertEqual(torneo_de_gallinas(estrategias), salida_esperada)

    def test_cuatro_jugadores(self):
        estrategias = {
            "carlos": "me la banco y no me desvio",
            "pablo": "me desvio siempre",
            "juan": "me desvio siempre",
            "mauro": "me la banco y no me desvio"
            }
        
        salida_esperada = {
            "carlos": 15,
            "pablo": -40,
            "juan": -40,
            "mauro": 15 
        }

        self.assertEqual(torneo_de_gallinas(estrategias), salida_esperada)

class ColaEnBancoTest(unittest.TestCase):
    def test_cola_mezclada(self):
        cola_original = Cola()
        cola_original.put(("carlos","comun"))
        cola_original.put(("pepe","vip"))
        cola_original.put(("maria","comun"))
        cola_original.put(("roberto","vip"))
        cola_original.put(("alicia","vip"))

        cola_esperada = Cola()
        cola_esperada.put("pepe")
        cola_esperada.put("roberto")
        cola_esperada.put("alicia")
        cola_esperada.put("carlos")
        cola_esperada.put("maria")

        self.assertEqual(reordenar_cola_priorizando_vips(cola_original).queue, cola_esperada.queue)

class SufijosPalindromos(unittest.TestCase):
    def test_obtener_sufijos(self):
        self.assertEqual(obtener_sufijos("que"), ["que", "ue", "e"])

    def test_holaeueueu(self):
        self.assertEqual(cuantos_sufijos_son_palindromos("holaeueueu"), 3)

class TaTeTiFacilito(unittest.TestCase):
    def test_consecutivos_en_lista(self):
        self.assertTrue(hay_consecutivos_en_lista(["O","X","X","X","O"], "X", 3))
        self.assertFalse(hay_consecutivos_en_lista(["O","X","X","X","O"], "O", 3))

    def test_tateti_5x5_gana_x(self):
        tablero = [
            ["X","O","X","",""],
            ["O","X","X","",""],
            ["X","X","O","",""],
            ["X","X","O","",""],
            ["O","O","X","O","O"]
        ]
        self.assertEqual(quien_gano_el_tateti_facilito(tablero), 1)

    def test_tateti_5x5_gana_o(self):
        tablero = [
            ["X","O","X","",""],
            ["O","X","O","",""],
            ["X","O","O","",""],
            ["X","X","O","",""],
            ["O","O","X","O","O"]
        ]
        self.assertEqual(quien_gano_el_tateti_facilito(tablero), 2)

    def test_tateti_5x5_empate(self):
        tablero = [
            ["X","O","X","",""],
            ["O","X","O","",""],
            ["X","O","X","",""],
            ["X","X","O","",""],
            ["O","O","X","O","O"]
        ]
        self.assertEqual(quien_gano_el_tateti_facilito(tablero), 0)

    def test_tateti_5x5_trampas(self):
        tablero = [
            ["O","O","X","",""],
            ["X","X","O","",""],
            ["X","O","O","",""],
            ["X","X","O","",""],
            ["O","O","X","O","O"]
        ]
        self.assertEqual(quien_gano_el_tateti_facilito(tablero), 3)


if __name__ == "__main__":
    unittest.main()