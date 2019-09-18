# -*- coding: utf-8 -*-


moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
gen = (coin for coin in moedas)

def valor_moedas(vlr, gen, lst):
    try:
        coin = next(gen)
        qtd = vlr  // coin
        lst.append((coin, int(qtd))) if qtd != 0 else None
        rst = vlr % coin
        valor_moedas(rst, gen, lst)
    except StopIteration:
        return dict(lst)

if __name__ == '__main__':
    lst = []
    valor_moedas(float(input()), gen, lst)
