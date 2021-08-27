
qtndPrimos = somaMultiplosTres = 0 
qtndParesMaioresVinte = somaParesMaioresVinte = 0 

for i in range(10):
	
	div = 0
	
	number = int(input("Número: "))
	
	if number % 3 == 0: 
		somaMultiplosTres += number
	
	if (number % 2 == 0 ) and (number > 20):
		somaParesMaioresVinte += number
		qtndParesMaioresVinte += 1 
	
	for p in range(1, number+1):
		
		if number % p == 0:
			div += 1
	
	if div == 2:
		qtndPrimos += 1

if qtndParesMaioresVinte > 0:
	mediaParesMaiorVinte = somaParesMaioresVinte / qtndParesMaioresVinte
	print("Média pares maiores que 20: {}".format(mediaParesMaiorVinte))

print("Quantidade de números primos: {}".format(qtndPrimos))	
print("Soma dos números múltiplos de três: {}".format(somaMultiplosTres))		

