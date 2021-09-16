"""
Faça um programa que preencha duas listas com 10 elementos em cada. 
Depois percorra essas duas listas e gere uma terceira lista com os 
números que se repetem nas duas listas. Mostre as três listas na tela.
"""

from random import randint

listaNumerosA = []
listaNumerosB = []
numerosRepetidos = [] 

for i in range(5):
    listaNumerosA.append(randint(1, 10))
    listaNumerosB.append(randint(1, 10))
    
for i in range(5):
	if listaNumerosA[i] in listaNumerosB:
		numerosRepetidos.append(listaNumerosA[i])
		
print(listaNumerosA)
print(listaNumerosB)
print(numerosRepetidos)
    


