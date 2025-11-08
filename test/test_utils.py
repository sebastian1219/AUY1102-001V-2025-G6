# tests/test_utils.py
import unittest
from utils import suma  # Importas la función que quieres probar

class TestUtils(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(2, 3), 5)

    def test_suma_negativos(self):
        self.assertEqual(suma(-1, -1), -2)

    def test_suma_mixtos(self):
        self.assertEqual(suma(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
