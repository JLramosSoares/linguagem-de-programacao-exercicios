"""
Escreva um programa que gere uma lista que é resultado do produto de 
duas listas L1 e L2. Mostre na tela as 3 listas.
"""

from random import randint

listaNumerosA = []
listaNumerosB = []
listaProdutos = []

for i in range(10):
    listaNumerosA.append(randint(1, 30))
    listaNumerosB.append(randint(1, 30))

for i in range(10):
     produto = listaNumerosA[i] * listaNumerosB[i]
     listaProdutos.append(produto)

print(listaNumerosA)
print(listaNumerosB)
print(listaProdutos)
