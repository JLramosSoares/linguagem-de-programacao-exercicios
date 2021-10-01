"""
Escreva um programa que leia uma matriz de ordem 3 x 5 de elementos inteiros, calcule e mostre na tela:
a) menor número da matriz;
b) soma dos números múltiplos de 3 da matriz;
c) média dos números da matriz;
"""

from random import randint

matriz = []
somaMultiplosTres = media = 0

for i in range(3):
    numeros = []
    for j in range(5):
        numeros.append(randint(1, 30))
    matriz.append(numeros)

for lista in matriz:
    print(lista)
 
for i in range(3):
    for j in range(5):
        if i == 0:
            menorNumero = matriz[i][j]

        if menorNumero > matriz[i][j]:
            menorNumero = matriz[i][j]

        if matriz[i][j] % 3 == 0:
            somaMultiplosTres += matriz[i][j]

        media += matriz[i][j]

media = media/15

print("\nMenor número: {}\nSoma número múltiplos de 3: {}".format(menorNumero, somaMultiplosTres))
print("Média da matriz: {}".format(media))
