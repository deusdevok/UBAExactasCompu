import unittest
from guia6_clase2 import volumen_esfera, triada_pitagorica

class test_volumen(unittest.TestCase):
    #se pueden definir los casos por separado
    def test_volumen_1(self):
        self.assertAlmostEqual(volumen_esfera(1.0), 4.1867, places=4)

    def test_volumen_nulo(self):
        self.assertAlmostEqual(volumen_esfera(0.0), 0.0, places=1)

    def test_volumen_5_25(self):
        self.assertAlmostEqual(volumen_esfera(5.25), 605.82375, places=5)
     
        
class test_triada_pitagorica(unittest.TestCase):
    def test_triada_verdadera_correcta(self):
        self.assertTrue(triada_pitagorica(3,4,5))

    def test_triada_falsa(self):
        self.assertFalse(triada_pitagorica(1,7,9))

    def test_triada_ok_desordenada(self):
        self.assertFalse(triada_pitagorica(5,4,3))

if __name__ == '__main__':
    unittest.main(verbosity=2)
