"""
Faça um programa que percorra duas listas e gere uma terceira lista sem 
os elementos repetidos. Mostra na tela as 3 listas.
"""

from random import randint

listaNumerosA = []
listaNumerosB = []
numerosNaoRepetidos = [] 

for i in range(5):
    listaNumerosA.append(randint(1, 10))
    listaNumerosB.append(randint(1, 10))
    
for i in range(5):
	if listaNumerosA[i] not in listaNumerosB:
		numerosNaoRepetidos.append(listaNumerosA[i])
	if listaNumerosB[i] not in listaNumerosA:
		numerosNaoRepetidos.append(listaNumerosB[i])

print(listaNumerosA)
print(listaNumerosB)
print(numerosNaoRepetidos)
