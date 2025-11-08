# test/test_config.py
import unittest
from src.config import cargar_configuracion

class TestConfig(unittest.TestCase):
    def test_entorno_valido(self):
        self.assertEqual(cargar_configuracion("dev"), {"modo": "dev"})

    def test_entorno_invalido(self):
        with self.assertRaises(ValueError):
            cargar_configuracion("test")
