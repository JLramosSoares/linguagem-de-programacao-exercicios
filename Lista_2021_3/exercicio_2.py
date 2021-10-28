"""
Escreva um programa que preencha uma matriz 4 x 6 com números inteiros, calcule e mostre na tela:
a) A quantidade de números que estão no intervalo entre 10 e 30
b) A soma dos números maiores que 10
c) A soma dos números que estão na quarta coluna da matriz
d) A média dos números da matriz que estão na terceira linha
"""

from random import randint

matriz = []
somaMaioresDez = somaQuartaColuna = entreDezETrinta = media = 0

for i in range(4):
    numeros = []
    for j in range(6):
        numeros.append(randint(1, 20))
    matriz.append(numeros)

for lista in matriz:
    print(lista)

for i in range(4):
    for j in range(6):

        if matriz[i][j] > 10:
            somaMaioresDez += matriz[i][j]
        if j == 3:
            somaQuartaColuna += matriz[i][j]
        if 10 < matriz[i][j] < 30:
            entreDezETrinta += 1
        if i == 2:
            media += matriz[i][j]

media = media/6


print("\nQuantidade entre 10 e 30: {}\nSoma maiores de 10: {}".format(entreDezETrinta, somaMaioresDez))
print("Soma dos numeros da quarta coluna: {}\nMédia da terceira linha: {}".format(somaQuartaColuna, media))
