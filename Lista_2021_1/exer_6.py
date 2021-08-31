idade = int(input("Idade: "))

qtndEntreVinteQuarenta = pessoas = somaIdades = 0 

while idade > 0:
	
	if pessoas == 0:
		maiorIdade = idade
		menorIdade = idade
	
	if 20 < idade < 40:
		qtndEntreVinteQuarenta += 1
	
	if idade > maiorIdade:
		maiorIdade = idade
	
	if idade < menorIdade:
		menorIdade = idade
	
	somaIdades += idade
	pessoas += 1

	idade = int(input("Idade: "))

mediaIdades = somaIdades / pessoas

if qtndEntreVinteQuarenta > 0:
	print("Qtnd idades entre 20 e 40: {}".format(qtndEntreVinteQuarenta))
	
print("Maior idade: {}".format(maiorIdade))
print("Menor idade: {}".format(menorIdade))
print("Média das idades: {}".format(mediaIdades))
	 
		
