"""
Faça um programa que percorra duas listas e gere uma terceira lista sem 
os elementos repetidos. Mostra na tela as 3 listas.
"""

from random import randint

listaNumerosA = []
listaNumerosB = []
numeroRepetidos = [] 

for i in range(5):
    listaNumerosA.append(randint(1, 10))
    listaNumerosB.append(randint(1, 10))
    
for number in listaNumerosA:
    
    verificador = 0
    
    for i in range(5):
        if number == listaNumerosA[i]:
            verificador += 1
        
    if verificador > 1:
        numeroRepetidos.append(number)
    
