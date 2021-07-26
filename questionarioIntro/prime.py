# -*- coding: utf-8 -*-
# Dado um número inteiro, dizer se é primo ou não.
# O programa implementa o algoritmo "Crivo de Eratóstenes"

from math import sqrt, floor

def primo(n):
    if n > 1:
        # O maior número a ser testado é floor(sqrt(n))
        testMax = floor(sqrt(n))
        for i in range(2, testMax+1):
            if n % i == 0:
                return "Não primo."
        return "Primo."
    else:
        return "Não primo."

print(primo(8))