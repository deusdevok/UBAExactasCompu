import unittest
from p7 import (
    pertenece1,
    pertenece2,
    pertenece3,
    divide_a_todos,
    suma_total,
    maximo,
    minimo,
    ordenados,
    pos_maximo,
    pos_minimo,
    long_mayorASiete,
    es_palindroma,
    iguales_consecutivos,
    vocales_distintas,
    pos_secuencia_ordenada_mas_larga,
    cantidad_digitos_impares,
    CerosEnPosicionesPares,
    CerosEnPosicionesPares2,
    sin_vocales,
    reemplaza_vocales,
    da_vuelta_str,
    eliminar_repetidos,
    resultadoMateria,
    saldoActual,
    pertenece_a_cada_uno_version_1,
    pertenece_a_cada_uno_version_2,
    pertenece_a_cada_uno_version_3,
    es_matriz,
    filas_ordenadas,
    columna,
    columnas_ordenadas,
    transponer,
    quien_gana_tateti,
)

# Ejercicio 1

class test_pertenece(unittest.TestCase):
    def test_pertenece1_ok(self):
        self.assertTrue(pertenece1([1,2,3], 1))

    def test_pertenece1_no_ok(self):
        self.assertFalse(pertenece1([1,2,3], 4))

    def test_pertenece1_lista_vacia(self):
        self.assertFalse(pertenece1([], 14))

    def test_pertenece1_lista_con_str(self):
        self.assertTrue(pertenece1(['a','b','c'], 'b'))

    def test_pertenece1_con_string(self):
        self.assertTrue(pertenece1("hola que tal", "q"))

    def test_pertenece2_ok(self):
        self.assertTrue(pertenece2([1,2,3], 1))

    def test_pertenece2_no_ok(self):
        self.assertFalse(pertenece2([1,2,3], 4))

    def test_pertenece2_lista_vacia(self):
        self.assertFalse(pertenece2([], 14))

    def test_pertenece3_ok(self):
        self.assertTrue(pertenece3([1,2,3], 1))

    def test_pertenece3_no_ok(self):
        self.assertFalse(pertenece3([1,2,3], 4))

    def test_pertenece3_lista_vacia(self):
        self.assertFalse(pertenece3([], 14))

class test_divide_a_todos(unittest.TestCase):
    def test_divide_a_todos_ok(self):
        self.assertTrue(divide_a_todos([4,8,16], 4))

    def test_divide_a_todos_false(self):
        self.assertFalse(divide_a_todos([4,9,16], 4))

class test_suma_total(unittest.TestCase):
    def test_suma_total_lista_vacia(self):
        self.assertEqual(suma_total([]), 0)

    def test_suma_total_lista_llena(self):
        self.assertEqual(suma_total([1,4,-3]), 2)

class test_maximo(unittest.TestCase):
    def test_maximo_lista_con_un_elemento(self):
        self.assertEqual(maximo([8]), 8)

    def test_maximo_lista_mas_de_un_elemento(self):
        self.assertEqual(maximo([-2,1,-8,18,3,0,2]), 18)

class test_minimo(unittest.TestCase):
    def test_minimo_lista_con_un_elemento(self):
        self.assertEqual(minimo([8]), 8)

    def test_minimo_lista_mas_de_un_elemento(self):
        self.assertEqual(minimo([-2,1,-8,18,3,0,2]), -8)

class test_ordenados(unittest.TestCase):
    def test_ordenados_lista_vacia(self):
        self.assertTrue(ordenados([]))

    def test_ordenados_lista_con_un_elemento(self):
        self.assertTrue(ordenados([5]))

    def test_ordenados_lista_desordenada(self):
        self.assertFalse(ordenados([6,5,8,9,11]))

    def test_ordenados_lista_ordenada(self):
        self.assertTrue([1,2,3,3,4,5,8,14,14,222])

class test_pos_maximo(unittest.TestCase):
    def test_pos_maximo_lista_vacia(self):
        self.assertEqual(pos_maximo([]), -1)

    def test_pos_maximo_un_elemento(self):
        self.assertEqual(pos_maximo([123]), 0)

    def test_pos_maximo_mas_de_un_elemento(self):
        self.assertEqual(pos_maximo([1,2,5,4,-9,3,0]), 2)

    def test_pos_maximo_varios_repetidos(self):
        self.assertEqual(pos_maximo([1,2,3,5,6,9,0,-2,9,1,9,3]), 5)

class test_pos_minimo(unittest.TestCase):
    def test_pos_minimo_lista_vacia(self):
        self.assertEqual(pos_minimo([]), -1)

    def test_pos_minimo_un_elemento(self):
        self.assertEqual(pos_minimo([123]), 0)

    def test_pos_minimo_mas_de_un_elemento(self):
        self.assertEqual(pos_minimo([1,2,5,4,-9,3,0]), 4)

    def test_pos_minimo_varios_repetidos(self):
        self.assertEqual(pos_minimo([1,2,3,-2,6,9,0,-2,9,1,9,3]), 3)

class test_long_mayorASiete(unittest.TestCase):
    def test_long_mayor_a_siete_lista_vacia(self):
        self.assertFalse(long_mayorASiete([]))

    def test_long_mayor_a_siete_palabras_cortas(self):
        self.assertFalse(long_mayorASiete(["hola", "vos"]))

    def test_long_mayor_a_siete_alguna_palabra_larga(self):
        self.assertTrue(long_mayorASiete(["hola", "cientifico", "que", "tal"]))

class test_palindroma(unittest.TestCase):
    def test_palindroma_string_vacio(self):
        self.assertTrue(es_palindroma(""))

    def test_palindroma_true_cant_impar(self):
        self.assertTrue(es_palindroma("neuquen"))

    def test_palindroma_true_cant_par(self):
        self.assertTrue(es_palindroma("anna"))

    def test_palindroma_false_cant_impar(self):
        self.assertFalse(es_palindroma("quetepasa"))

    def test_palindroma_false_cant_par(self):
        self.assertFalse(es_palindroma("quetepasa!"))

class test_iguales_consecutivos(unittest.TestCase):
    def test_iguales_consecutivos_long_menor_3(self):
        self.assertFalse(iguales_consecutivos([4,4]))

    def test_iguales_consecutivos_false(self):
        self.assertFalse(iguales_consecutivos([1,2,4,2,6,2,1,1,2,2]))

    def test_iguales_consecutivos_igual_a_3_true(self):
        self.assertTrue(iguales_consecutivos([1,2,3,7,7,7,9,0]))

    def test_iguales_consecutivos_mayor_a_3_true(self):
        self.assertTrue(iguales_consecutivos([1,2,3,7,7,7,7,9,0]))

    def test_iguales_consecutivos_al_final(self):
        self.assertTrue(iguales_consecutivos([1,2,3,7,8,4,4,6,4,4,4]))

class test_vocales_distintas(unittest.TestCase):
    def test_vocales_distintas_string_vacio(self):
        self.assertFalse(vocales_distintas(""))

    def test_vocales_distintas_dos_vocales_distintas(self):
        self.assertFalse(vocales_distintas("holaholahola"))

    def test_vocales_distintas_tres_vocales_distintas(self):
        self.assertTrue(vocales_distintas("holaamiguitoquehaces"))

class test_pos_secuencia_ordenada_mas_larga(unittest.TestCase):
    def test_sec_mas_larga_un_elemento(self):
        self.assertEqual(pos_secuencia_ordenada_mas_larga([6]), 0)

    def test_sec_mas_larga_todos_ordenados(self):
        self.assertEqual(pos_secuencia_ordenada_mas_larga([1,2,3,7,99]), 0)

    def test_sec_mas_larga_todos_desordenados(self):
        self.assertEqual(pos_secuencia_ordenada_mas_larga([3,2,1]), 0)

    def test_sec_mas_larga_unica(self):
        self.assertEqual(pos_secuencia_ordenada_mas_larga([8,0,1,2,0,3,4,5,6,7,4,3,7,8,9,3,7]), 4)

    def test_sec_mas_larga_unica_2(self):
        self.assertEqual(pos_secuencia_ordenada_mas_larga([8,0,1,2,0,3,4,5,6,7,4,3,7,8,9,10,11,12,3,7]), 11)

    def test_sec_mas_larga_repetida(self):
        self.assertEqual(pos_secuencia_ordenada_mas_larga([8,0,1,2,0,3,4,5,6,7,4,3,7,8,9,10,11,3,7]), 4)

class test_cantidad_digitos_impares(unittest.TestCase):
    def test_cant_digitos_impares_lista_vacia(self):
        self.assertEqual(cantidad_digitos_impares([]), 0)

    def test_cant_digitos_impares_cero_impares(self):
        self.assertEqual(cantidad_digitos_impares([44, 226, 8, 640]), 0)

    def test_cant_digitos_impares_algunos_impares(self):
        self.assertEqual(cantidad_digitos_impares([57, 2383, 812, 246]), 5)

# Ejercicio 2

class test_ceros_en_posiciones_pares(unittest.TestCase):
    def test_ceros_pos_par(self):
        s = [1,2,3,4]
        CerosEnPosicionesPares(s)
        self.assertEqual(s, [0,2,0,4])

class test_ceros_en_posiciones_pares2(unittest.TestCase):
    def test_ceros_pos_par_no_cambia_entrada(self):
        s = [1,2,3,4]
        CerosEnPosicionesPares2(s)
        self.assertEqual(s, [1,2,3,4])

    def test_ceros_pos_par_salida(self):
        s = [1,2,3,4]
        self.assertEqual(CerosEnPosicionesPares2(s), [0,2,0,4])

class test_sin_vocales(unittest.TestCase):
    def test_sin_vocales_string_vacio(self):
        self.assertEqual(sin_vocales(""), "")

    def test_sin_vocales_string_sin_vocales(self):
        self.assertEqual(sin_vocales("rts"), "rts")

    def test_sin_vocales_string_todas_vocales(self):
        self.assertEqual(sin_vocales("aeoooo"), "")

    def test_sin_vocales_mix(self):
        self.assertEqual(sin_vocales("hola como andas todo bien?"), "hl cm nds td bn?")

class test_reemplaza_vocales(unittest.TestCase):
    def test_reemplaza_vocales_mix(self):
        self.assertEqual(reemplaza_vocales("hola que ase"), "h_l_ q__ _s_")

class test_da_vuelta_str(unittest.TestCase):
    def test_da_vuelta_str_vacio(self):
        self.assertEqual(da_vuelta_str(""), "")

    def test_da_vuelta_str_largo(self):
        self.assertEqual(da_vuelta_str("hola pibe"), "ebip aloh")

class test_eliminar_repetidos(unittest.TestCase):
    def test_eliminar_repetidos_vacio(self):
        self.assertEqual(eliminar_repetidos(""), "")

    def test_eliminar_repetidos_sin_repes(self):
        self.assertEqual(eliminar_repetidos("hola pibe"), "hola pibe")

    def test_eliminar_repetidos_con_repes(self):
        self.assertEqual(eliminar_repetidos("hola hola como andas che?"), "hola cmndse?")

    
class TestResultadoMateria(unittest.TestCase):
    def test_resultado_materia_promedio_mayor_7(self):
        self.assertEqual(resultadoMateria([4,10,4,9,9,8,9]), 1)

    def test_resultado_materia_promedio_entre_4_y_7(self):
        self.assertEqual(resultadoMateria([4,5,6,7]), 2)

    def test_resultado_materia_promedio_menor_4(self):
        self.assertEqual(resultadoMateria([1,2,3,5,1,1,1]), 3)

class TestSaldoActual(unittest.TestCase):
    def test_saldo_actual_sin_movimientos(self):
        self.assertEqual(saldoActual([]), 0)

    def test_saldo_actual_1_ingreso(self):
        self.assertEqual(saldoActual([("I", 150)]), 150)

    def test_saldo_actual_retiro_mayor_ingreso(self):
        self.assertEqual(saldoActual([("I", 100), ("R", 200)]), 0)

    def test_saldo_actual_positivo(self):
        self.assertEqual(saldoActual([("I",2000), ("R",20), ("R",1000), ("I",300)]), 1280)

class TestPerteneceACadaUnoV1(unittest.TestCase):
    def test_pertenece_a_c_u_v1_res_mas_grande_que_s(self):
        res = [False,False,False]
        pertenece_a_cada_uno_version_1([[3]], 3, res)
        self.assertEqual(res, [True,False,False])

    def test_pertenece_a_c_u_v1_res_igual_que_s(self):
        res = [False]
        pertenece_a_cada_uno_version_1([[3]], 3, res)
        self.assertEqual(res, [True])

    def test_pertenece_a_c_u_v1_res_mas_chica_que_s(self):
        res = []
        pertenece_a_cada_uno_version_1([[3]], 3, res)
        self.assertEqual(res, [True])

    def test_pertenece_a_c_u_v1_res_mas_chica_que_s_mix(self):
        res = [True, False]
        pertenece_a_cada_uno_version_1([[2], [3,2], [1,2,3]], 3, res)
        self.assertEqual(res, [False, True, True])

class TestPerteneceACadaUnoV2(unittest.TestCase):
    def test_pertenece_a_c_u_v2_res_mas_grande_que_s(self):
        res = [False,False,False]
        pertenece_a_cada_uno_version_2([[3]], 3, res)
        self.assertEqual(res, [True])

    def test_pertenece_a_c_u_v2_res_igual_que_s(self):
        res = [False]
        pertenece_a_cada_uno_version_2([[3]], 3, res)
        self.assertEqual(res, [True])

    def test_pertenece_a_c_u_v2_res_mas_chica_que_s(self):
        res = []
        pertenece_a_cada_uno_version_2([[3]], 3, res)
        self.assertEqual(res, [True])

    def test_pertenece_a_c_u_v2_res_mas_chica_que_s_mix(self):
        res = [True, False]
        pertenece_a_cada_uno_version_2([[2], [3,2], [1,2,3]], 3, res)
        self.assertEqual(res, [False, True, True])

class TestPerteneceACadaUnoV3(unittest.TestCase):
    def test_pertenece_a_c_u_v3_unico_elem(self):
        self.assertEqual(pertenece_a_cada_uno_version_3([[3]], 3), [True])

    def test_pertenece_a_c_u_v3_muchos(self):
        self.assertEqual(pertenece_a_cada_uno_version_3([[3],[1,1,2],[9,3,0]], 3), [True,False,True])

    def test_pertenece_a_c_u_v3_vacio(self):
        self.assertEqual(pertenece_a_cada_uno_version_3([], 80), [])
    
class TestEsMatriz(unittest.TestCase):
    def test_es_matriz_vacia(self):
        self.assertFalse(es_matriz([]))

    def test_es_matriz_fila_vacia(self):
        self.assertFalse(es_matriz([[]]))

    def test_es_matriz_unico_elemento(self):
        self.assertTrue(es_matriz([[1]]))

    def test_es_matriz_filas_distintas(self):
        self.assertFalse(es_matriz([[1,2,3],[4,5]]))

    def test_es_matriz_ok(self):
        self.assertTrue(es_matriz([[1,2,3],[4,5,6]]))

class TestFilasOrdenadas(unittest.TestCase):
    def test_filas_ord_ok(self):
        res = [True,False]
        filas_ordenadas([[1,2,3],[6,7,8],[1,6,99]], res)
        self.assertEqual(res, [True,True,True])

    def test_filas_ord_mix(self):
        res = [True,False]
        filas_ordenadas([[1,2,3],[6,7,0],[1,6,99]], res)
        self.assertEqual(res, [True,False,True])

class TestColumna(unittest.TestCase):
    def test_columna_ok(self):
        self.assertEqual(columna([[1,2,3],[4,5,6],[0,0,0]], 1), [2,5,0])

class TestColumnasOrdenadas(unittest.TestCase):
    def test_columnas_ordenadas_mix(self):
        self.assertEqual(
            columnas_ordenadas([[1,2,3],[2,1,4],[3,9,9]]),
            [True, False, True]
        )

class TestTransponer(unittest.TestCase):
    def test_transponer_ok(self):
        self.assertEqual(transponer([[1,2,3],[4,5,6]]), [[1,4],[2,5],[3,6]])

class TestTaTeTi(unittest.TestCase):
    def test_tateti_gana_o_fila(self):
        m = [
            ["O","O","O"],
            ["X","X","O"],
            ["O","X","X"],
        ]
        self.assertEqual(quien_gana_tateti(m), 0)

    def test_tateti_gana_x_columna(self):
        m = [
            ["X","O","O"],
            ["X","O","X"],
            ["X","X","O"],
        ]
        self.assertEqual(quien_gana_tateti(m), 1)

    def test_tateti_gana_o_diag(self):
        m = [
            ["O","O","X"],
            ["X","O","X"],
            ["X","X","O"],
        ]
        self.assertEqual(quien_gana_tateti(m), 0)

    def test_tateti_gana_x_diag(self):
        m = [
            ["X","O","O"],
            ["O","X","X"],
            ["X","O","X"],
        ]
        self.assertEqual(quien_gana_tateti(m), 1)

    def test_tateti_empate(self):
        m = [
            ["X","O","O"],
            ["O","O","X"],
            ["X","X","O"],
        ]
        self.assertEqual(quien_gana_tateti(m), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)