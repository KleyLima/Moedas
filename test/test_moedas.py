# -*- coding: utf-8 -*-

import unittest
from source.moedas import Moedas

class TestMoeda(unittest.TestCase):
    def test_moeda(self):
        """
        Método para testar a função de converter valor para moedas, testa diferentes aspectos da função.
        """
        self.assertEqual(Moedas(9.99).valor_moedas(), [(1, 9), (0.5, 1), (0.25, 1), (0.1, 2), (0.01, 4)])  # valor 9.99
        self.assertEqual(Moedas(0.09).valor_moedas(), [(0.05, 1), (0.01, 4)])  # valor 0.09
        self.assertEqual(Moedas('008').valor_moedas(), [(1, 8)])  # valor sem ponto
        self.assertFalse(Moedas(-88.88).valor_moedas())  # valor negativo
        self.assertFalse(Moedas('abc').valor_moedas())

if __name__ == '__main__':
    unittest.main()


