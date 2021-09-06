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
    
for number in listaNumerosA:
    
    verificadorListaA = 0
    verificadorListaB = 0
    
    for i in range(5):
        if number == listaNumerosA[i]:
            verificadorListaA += 1
        
    if verificadorListaA > 1:
        if number not in numerosRepetidos:
            numerosRepetidos.append(number)
    
for number in listaNumerosB:
	
	verificadorListaA = 0
	verificadorListaB = 0
	
	for i in range(5):
		if number == listaNumerosB[i]:
			verificadorListaB += 1
			
	if verificadorListaB > 1:
		if number not in numerosRepetidos:
			numerosRepetidos.append(number)

print(listaNumerosA)
print(listaNumerosB)
print(numerosRepetidos)


