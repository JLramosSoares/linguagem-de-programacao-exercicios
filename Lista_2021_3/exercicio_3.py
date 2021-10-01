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

for i in range(4):
    vendedores.append(input("Nome vendedor: "))

matriz.append(vendedores)

for i in range(4):
    vendas = []
    for j in range(4):
        vendas.append(randint(800, 3000))
    matriz.append(vendas)

for linha in matriz:
    print(linha)       


