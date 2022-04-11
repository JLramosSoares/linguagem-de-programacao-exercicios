"""
1) Faça um programa em Python para construir uma matriz identidade
ordem 100 (cem linhas e cem colunas) usando NumPy. Caso haja
dificuldade na instalação, use https://onecompiler.com/python para
testar seu programa antes de entregar (exe_01.py).
"""

import numpy as np

matrix = np.ndarray((100, 100), dtype = np.int64)

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if i == j:
            matrix[i, j] = 1
        else:
            matrix[i, j] = 0

print(matrix)