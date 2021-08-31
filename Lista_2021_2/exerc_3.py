"""
Faça um programa que preencha duas listas, lista A e lista B com 5 
números em cada. Gere a lista C, com os números da lista A e lista B. 
Depois calcule e mostre na tela a quantidade de números perfeitos. 
Um número é perfeito quando ele é igual a soma dos seus divisores 
excetuando ele próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são 
seus divisores).
"""

from random import randint

lista_A = []
lista_B = []

for i in range(5):	
	lista_A.append(randint(1, 100))
	lista_B.append(randint(1, 100))

lista_C = lista_A + lista_B

contadorNumerosPerfeitos = 0

for numero in lista_C:
	
	somaDivisores = 0
	
	for i in range(1, numero):
		if numero % i == 0:
			somaDivisores += i
		
	if somaDivisores == numero:
		contadorNumerosPerfeitos += 1
		print(numero)
	
print("Quantidade de números perfeitos: {}".format(contadorNumerosPerfeitos))
