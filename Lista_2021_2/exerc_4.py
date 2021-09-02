"""
Faça um programa que preencha duas listas com 10 elementos em cada. 
Depois percorra essas duas listas e gere uma terceira lista com os 
números que se repetem nas duas listas. Mostre as três listas na tela.
"""

from random import randint

listaNumerosA = []
listaNumerosB = []
listaNumerosRepetidos = []

for i in range(10):    
    listaNumerosA.append(randint(1, 500))
    listaNumerosB.append(randint(1, 500))
    
for i in range(10):
    
    verificarNumerosRepetidos = listaNumerosA[i]
    
    for number in listaNumerosA:
        if verificarNumerosRepetidos == number:
            listaNumerosRepetidos.append(listaNumerosA[i])
    
