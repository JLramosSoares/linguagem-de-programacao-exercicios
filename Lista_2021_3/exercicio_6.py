"""
Escreva um programa que leia uma matriz 6 x 10, 
some as colunas individualmente e acumule as somas na 7ª linha da matriz.
O programa deverá mostrar o resultado de cada coluna.
"""

from random import randint

mat = []
somaColunas = [0]*10

for i in range(5):
    mat.append([0]*10)

for i in range(5):
    for j in range(10):
        mat[i][j] = randint(1, 50)

for i in range(5):
    for j in range(10): 
        if j == j:
            somaColunas[j] += mat[i][j]  

mat.append(somaColunas)

for linha in mat:
    print(linha)