"""
Escreva um programa que leia uma matriz de ordem 5 x 4, onde na 1ª coluna da 
matriz são armazenados os nomes dos vendedores, da 2ª coluna a 4ª coluna dão armazenados 
as total de vendas por mês de cada vendedor, portando na 2ª coluna é armazenado a venda do 
mês 1, 3ª coluna do mês 2 e na 4ª coluna do mês 3. Calcule e mostre na tela:

a) O valor total vendido por vendedor
b) A maior venda do mês 1
c) A menor venda do mês 3
d) O total vendido por mês
"""

from random import randint

matriz = []
vendedores = []

for i in range(5):
    linha = []
    for j in range(4):
        linha = [0] * 4
    matriz.append(linha)

for i in range(5):
    vendedores.append(input("Nome do vendedor: "))

for i in range(5):
    for j in range(4):
        if j == 0:
            matriz[i][j] = vendedores[i]
        else:
            matriz[i][j] = randint(800, 3000)

for linha in matriz:
    print(linha)

for i in range(1, 3):
    for j in range(1, 4): 

        if j == 3:
            if menorVendaMesTres > matriz[i][j]:
                menorVendaMesTres = matriz[i][j]

        if j == 1:
            maiorVendaMesUm = matriz[i][j]
        
        if (maiorVendaMesUm < matriz[i][j]) and (j == 1):
            maiorVendaMesUm = matriz[i][j]

print("Maior venda do mês um: {}\nMenor venda do mês três: {}".format(maiorVendaMesUm, menorVendaMesTres))
