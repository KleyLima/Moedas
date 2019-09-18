# -*- coding: utf-8 -*-

import unittest

class TestMoeda(unittest.TestCase):
    def test_moeda():
    """
    Método para testar a função de converter valor para moedas, testa diferentes aspectos da função.
    """
        self.assertEqual(Moeda(9.99).moeda, {'1': '9', '0.50': '1', '0.25': '1', '0.10': '2', '0.05': '0', '0.01': '0'})  # valor 9.99
        self.assertEqual(Moeda(0.09).moeda, {'1': '0', '0.50': '0', '0.25': '0', '0.10': '0', '0.05': '1', '0.01': '4'})  # valor 0.09
        self.assertEqual(Moeda(009).moeda, {'1': '9', '0.50': '0', '0.25': '0', '0.10': '0', '0.05': '0', '0.01': '0'})  # valor sem ponto
        self.assertFalse(Moeda(-88.88).moeda)  # valor negativo
        
        
class Moeda:
    @classmethod
    def __init__(cls, vlr):
        cls.moeda = cls.valor_moedas(vlr)
     
    @classmethod
    def valor_moedas(cls, vlr):
        coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
        asw = {coin for coin in coins}
