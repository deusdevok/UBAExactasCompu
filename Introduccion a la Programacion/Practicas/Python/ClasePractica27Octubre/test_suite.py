import unittest
from ej9 import sumar
from ej11 import triangle

class TestSumar(unittest.TestCase):
    def test_sumar_cero(self):
        self.assertEqual(sumar(3,0), 3, "test_sumar_cero")

    def test_sumar_neg(self):
        self.assertEqual(sumar(3,-2), 1)

class TestTriangulo(unittest.TestCase):
    def test_triangulo_invalido_a(self):
        self.assertEqual(triangle(-1,1,1), 4)
    
    def test_triangulo_invalido_b(self):
        self.assertEqual(triangle(1,2,10), 4)

    def test_triangulo_equilatero(self):
        self.assertEqual(triangle(2,2,2), 1)

    def test_triangulo_isosceles(self):
        self.assertEqual(triangle(1,3,3), 2)

    def test_triangulo_escaleno(self):
        self.assertEqual(triangle(3,4,5), 3)

if __name__ == "__main__":
    unittest.main()