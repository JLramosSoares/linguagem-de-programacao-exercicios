"""
Escreva um programa que preencha uma matriz 4 x 3 com números inteiros, calcule e mostre na tela:
a) A soma dos elementos que estão na 2ª e 4ª linha da matriz
b) A soma dos números primos
"""

from random import randint

matriz = []
somaSegundaQuartaLinha = 0
somaPrimos = 0

for i in range(4):
    linha = []
    for j in range(3):
        linha.append(randint(1, 50))
    matriz.append(linha)

for linha in matriz:
    print(linha)

for i in range(4):
    for j in range(3):

        cont = 0
        for k in range(1, matriz[i][j]+1):
            if matriz[i][j] % k == 0:
                cont += 1
        
        if cont == 2:
            somaPrimos += matriz[i][j]

        if i == 1:
            somaSegundaQuartaLinha += matriz[i][j]
        if i == 3:
            somaSegundaQuartaLinha += matriz[i][j]

print("\nSoma da segunda e terceira linha: {}\nSoma dos primos: {}".format(somaSegundaQuartaLinha, somaPrimos))
