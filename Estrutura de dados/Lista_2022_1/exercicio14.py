"""
14) Crie uma função recursiva para somar todos os números de 1 a n (inclusive). Teste com n = 100.
"""

def soma(n:int) -> int:
    if n == 1:
        return 1
    else:
        somaAcumulada = n + soma(n - 1)
    return somaAcumulada

print("Soma:",soma(100))