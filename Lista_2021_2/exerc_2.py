"""
Faça um programa que preencha uma lista com 10 cores diferentes. Depois 
permita fazer uma pesquisa se uma determinada cor existe armazenada na 
lista, se existir deve ser impresso na tela a cor e em qual posição 
(índice) esta cor está armazenada. A pesquisa deve ser feita até que 
seja digitado FIM na cor a ser pesquisada na lista.
"""

cores = []

for i in range(10):
	cores.append(input("Cor: ").upper())

cor = input("\nDigite o nome de uma cor: ").upper()
while cor != "FIM":
	if cor.upper() in cores:
		print("\nA cor {} está no índice {} da lista".format(cor,cores.index(cor)))
	
	cor = input("\nDigite o nome de uma cor: ").upper()
		 
