"""
Faça um programa que preencha duas listas com 10 elementos em cada. 
Depois percorra essas duas listas e gere uma terceira lista com os 
números que se repetem nas duas listas. Mostre as três listas na tela.
"""
from random import randint

listaNumerosA = []
listaNumerosB = []
numerosRepetidos = []

for i in range(10):
	listaNumerosA.append(randint(1, 30))
	listaNumerosB.append(randint(1, 30))

for i in range(10):
	for number in listaNumerosA:
		if number == listaNumerosB[i]:
			numerosRepetidos.append(number)
