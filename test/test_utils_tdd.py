# test/test_utils_tdd.py
import unittest
from utils import suma

class TestSumaTDD(unittest.TestCase):
    def test_suma_tipo_invalido(self):
        with self.assertRaises(TypeError):
            suma("2", 3)

    def test_suma_valida(self):
        self.assertEqual(suma(5, 7), 12)

    def test_suma_decimal(self):
        self.assertAlmostEqual(suma(2.5, 3.5), 6.0)

    def test_suma_negativos(self):
        self.assertEqual(suma(-4, -6), -10)

    def test_suma_cero(self):
        self.assertEqual(suma(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
