from random import randint

for i in range(1, 11):
	
	div = 0
	
	if i == 1:
		somaPrimos = qtndMultres = somaMultres = 0
		somaMaiorIgualDezTrinta = qtndSomaMaiorIgualDezTrinta = 0
	
	number = randint(1,50)
	
	if (number % 3 == 0) and (number > 10):
		somaMultres += number
		qtndMultres += 1
	
	if 10 <= number <= 30:
		somaMaiorIgualDezTrinta += number
		qtndSomaMaiorIgualDezTrinta += 1

	for p in range(1, number+1):
		if number % p == 0:
			div += 1
	
	if div == 2:
		somaPrimos += number


print("*{}".format(somaPrimos))

if qtndMultres > 0:
	medMultTresMaiorDez = somaMultres / qtndMultres
	print("*{}".format(medMultTresMaiorDez))
	
if qtndSomaMaiorIgualDezTrinta > 0:
	medMaiorIgualDezTrinta = somaMaiorIgualDezTrinta/qtndSomaMaiorIgualDezTrinta
	print("*{}".format(medMaiorIgualDezTrinta))

