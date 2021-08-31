"""
Escreva um programa que leia a idade de 10 pessoas e armazene-as em uma 
lista. Calcule e mostre:
a) a menor idade
b) a média das idades
c) a quantidade de pessoas que tem idade entre 20 e 30 anos (inclusive)
d) a quantidade de pessoas com idade maior que a média
"""

from random import randint

idades = []

for i in range(10):
	idades.append(randint(1, 120))

for i in range(len(idades)):
	
	if i == 0:
		menorIdade = idades[i]
		idadesEntreVinteTrinta = 0 
		quantidadeIdadesMaiorMedia = 0
	
	if menorIdade > idades[i]:
		 menorIdade = idades[i]
	
	if 20 >= idades[i] <= 30:
		idadesEntreVinteTrinta += 1

mediaGeral = sum(idades)/10

for idade in idades:
	
	if idade > mediaGeral:
		quantidadeIdadesMaiorMedia += 1

print("Menor idade: {}".format(menorIdade))
print("Média das idades: {}".format(mediaGeral))
print("Quantidade de pessoas entre 20 e 30 (inclusive): {}".format(idadesEntreVinteTrinta))
print("Quantidade pessoas acima da média de idades: {}".format(quantidadeIdadesMaiorMedia))
