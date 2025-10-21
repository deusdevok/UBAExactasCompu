import unittest
from p6testing import (
    suma, 
    triada_pitagorica, 
    es_multiplo_de, 
    devolver_el_doble_si_es_par, 
    fahrenheit_a_celsius,
    es_primo,
    cantidad_primos_en_rango
)

class test_sumar(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(2,3), 5)

    def test_suma_negativos(self):
        self.assertEqual(suma(-4,-7), -11)

class test_triada_pitagorica(unittest.TestCase):
    def test_triada_verdadera_correcta(self):
        self.assertTrue(triada_pitagorica(3,4,5))

    def test_triada_falsa(self):
        self.assertFalse(triada_pitagorica(1,7,9))

    def test_triada_ok_desordenada(self):
        self.assertFalse(triada_pitagorica(5,4,3))

class test_es_multiplo_de(unittest.TestCase):
    def test_son_multiplos(self):
        self.assertTrue(es_multiplo_de(6, 3))

    def test_no_son_multiplos(self):
        self.assertFalse(es_multiplo_de(15, 4))

class test_devolver_el_doble_si_es_par(unittest.TestCase):
    def test_devuelve_doble_con_numero_par(self):
        self.assertEqual(devolver_el_doble_si_es_par(4), 8)

    def test_devuelve_mismo_numero_con_impar(self):
        self.assertEqual(devolver_el_doble_si_es_par(7), 7)

class test_fahrenheit_a_celsius(unittest.TestCase):
    def test_32_fahrenheit_igual_a_0_celsius(self):
        self.assertEqual(fahrenheit_a_celsius(32), 0)

    def test_mayor_a_32_fahrenheit_a_celsius(self):
        self.assertGreater(fahrenheit_a_celsius(40), 0)

    def test_menor_a_32_fahrenheit_a_celsius(self):
        self.assertLess(fahrenheit_a_celsius(27), 0)

    def test_212_fahrenheit_da_100_celsius(self):
        self.assertEqual(fahrenheit_a_celsius(212), 100)

    def test_fahrenheit_positivo(self):
        self.assertAlmostEqual(fahrenheit_a_celsius(48), 8.89, places=2)

class test_es_primo(unittest.TestCase):
    def test_positivo_es_primo(self):
        self.assertTrue(es_primo(17))

    def test_positivo_no_es_primo(self):
        self.assertFalse(es_primo(25))

    def test_negativo_no_es_primo(self):
        self.assertFalse(es_primo(-12))

    def test_uno_no_es_primo(self):
        self.assertFalse(es_primo(1))

    def test_cero_no_es_primo(self):
        self.assertFalse(es_primo(0))

class test_cantidad_primos_en_rango(unittest.TestCase):
    def test_cant_primos_entre_dos_valores_ordenados(self):
        self.assertEqual(cantidad_primos_en_rango(8, 2), 4)

    def test_cant_primos_entre_dos_valores_desordenados(self):
        self.assertEqual(cantidad_primos_en_rango(2, 8), 4)

    def test_cant_primos_entre_dos_valores_uno_negativo(self):
        self.assertEqual(cantidad_primos_en_rango(-3, 4), 2)

    def test_cant_primos_entre_dos_valores_iguales(self):
        self.assertEqual(cantidad_primos_en_rango(11, 11), 1)

    def test_cant_primos_cero_en_limite_de_rango(self):
        self.assertEqual(cantidad_primos_en_rango(0, 4), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)