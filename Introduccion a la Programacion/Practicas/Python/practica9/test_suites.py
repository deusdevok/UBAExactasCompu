import unittest
from programas import *


class TestMax(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max2(0,0), 0)

    def test_max_2(self):
        self.assertEqual(max2(0,1), 1)

class TestMin(unittest.TestCase):
    def test_min_a(self):
        self.assertEqual(min2(0,1), 0)

    def test_min_b(self):
        self.assertEqual(min2(1,1), 1)
    
    def test_min_c(self):
        self.assertEqual(min2(1,0), 0)

class TestSuma(unittest.TestCase):
    def test_suma_a(self):
        self.assertEqual(sumar(1,2), 3)

class TestResta(unittest.TestCase):
    def test_resta_a(self):
        self.assertEqual(restar(1,0), 1)

    def test_resta_b(self):
        self.assertEqual(restar(1,2), -1)

class TestSigno(unittest.TestCase):
    def test_signo_a(self):
        self.assertEqual(signo(5), 1)

    def test_signo_b(self):
        self.assertEqual(signo(-5), -1)

    def test_signo_c(self):
        self.assertEqual(signo(0), 0)

class TestFabs6(unittest.TestCase):
    def test_fabs6_a(self):
        self.assertEqual(fabs6(-3), 3)

    def test_fabs6_b(self):
        self.assertEqual(fabs6(0), 0)

    def test_fabs6_c(self):
        self.assertEqual(fabs6(3), 3)

class TestFabs7(unittest.TestCase):
    def test_fabs7_a(self):
        self.assertEqual(fabs7(-3), 3)

    def test_fabs7_b(self):
        self.assertEqual(fabs7(3), 3)

class TestMult10(unittest.TestCase):
    def test_mult10_a(self):
        self.assertEqual(mult10(5), 50)

class TestSumar9(unittest.TestCase):
    def test_sumar9_a(self):
        self.assertEqual(sumar9(2,3), 5)

    def test_sumar9_b(self):
        self.assertEqual(sumar9(2,-3), -1)

class TestMCD(unittest.TestCase):
    def test_mcd_a(self):
        self.assertEqual(mcd(3,5), 15)

class TestTriangle(unittest.TestCase):
    def test_triangle_a(self):
        self.assertEqual(triangle(-1,1,1), 4)

    def test_triangle_b(self):
        self.assertEqual(triangle(1,2,4), 4)

    def test_triangle_c(self):
        self.assertEqual(triangle(2,2,2), 1)

    def test_triangle_d(self):
        self.assertEqual(triangle(3,3,2), 2)

    def test_triangle_e(self):
        self.assertEqual(triangle(3,4,5), 3)

class TestMultByAbs(unittest.TestCase):
    def test_mult_by_abs_a(self):
        self.assertEqual(multByAbs(2,-3), 6)

class TestVaciarSecuencia(unittest.TestCase):
    def test_vaciar_secuencia_a(self):
        s = [1,2,3]
        vaciarSecuencia(s)
        self.assertEqual(s, [0,0,0])

class TestExisteElemento(unittest.TestCase):
    def test_existe_elemento_a(self):
        self.assertTrue(existeElemento([1,2,3,4], 2))

    def test_existe_elemento_b(self):
        self.assertTrue(existeElemento([1,2,3,4], 4))

    def test_existe_elemento_c(self):
        self.assertFalse(existeElemento([1,2,3,4], 5))

# if __name__ == "__main__":
#     unittest.main(verbosity=2)