# -*- coding: utf-8 -*-

from sys import exit


class Moedas:
    """ Classe que representa as moedas, seus valores e relação na sua distribuição dado um valor."""

    @classmethod
    def __init__(cls, vlr):
        """
        Método que inicializa os atributos da classe, define as moedas disponiveis para distribuição e um 
        gerador de moedas, util na recursividade da funcão de transformação.
        """
        cls.vlr = cls.check(vlr)
        cls.moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
        cls.gen = (coin for coin in cls.moedas)
        cls.lst = []

    @classmethod
    def valor_moedas(cls):
        """
        Distribui o valor passado para conversão na configuração de moedas presente em cls.moedas, usa o cls.gen
        para iterar sobre os valores a cada chamada recursiva da função. Retorna um dicionário das moedas
        utilizadas na tela.
        """
        try:
            coin = next(cls.gen)
            qtd = cls.vlr // coin
            cls.lst.append((coin, int(qtd))) if qtd != 0 else None
            cls.vlr %= coin
            cls.vlr = round(cls.vlr, 2)
            cls.valor_moedas()
        except StopIteration:
            return cls.lst
        finally:
            return cls.lst if cls.lst else False

    @classmethod
    def check(cls, vlr):
        try:
            vlr = float(vlr)
            return vlr if vlr > 0 else False
        except ValueError:
            return False


if __name__ == '__main__':
    print(Moedas(input()).valor_moedas())
