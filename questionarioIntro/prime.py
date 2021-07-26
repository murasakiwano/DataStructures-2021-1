# -*- coding: utf-8 -*-
# Dado um número inteiro, dizer se é primo ou não.
# O programa implementa o algoritmo "Crivo de Eratóstenes"

from math import sqrt, floor

def primo(n):
    # O maior número a ser testado é floor(sqrt(n))
    maximo = floor(sqrt(n))
    if n > 1: # 1 não é primo
        l = list(range(2, n + 1))
        i = 0
        test = 2
        while True:
            test = l[i]
            if test <= maximo:
                for x in l[i+1:]:
                    if x % test == 0:
                      l.remove(x)
                i = i + 1
            else:
                break
        if n in l:
            return "Primo."
        else:
            return "Não primo."
    else:
        return "Não primo."

print(primo(8))