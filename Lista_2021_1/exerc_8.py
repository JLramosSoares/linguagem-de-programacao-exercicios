from random import randint

idadesInferioresDezoito = pessoasMaioresOitentaQuilos = 0 
somaAlturaTodos = 0 
somatoriaIdadesTimeUm = 0
somatoriaIdadesTimeDois = 0 
somatoriaIdadesTimeTres = 0
somatoriaIdadesTimeQuatro = 0
somatoriaIdadesTimeCinco = 0

for i in range(1,5):
	
	if i == 1:
		print("\nTIME UM")
		
	if i == 2:
		print("\nTIME DOIS")
		
	if i == 3:
		print("\nTIME TRÊS")
		
	if i == 4:
		print("\nTIME QUATRO")
		
	if i == 5:
		print("\nTIME CINCO")

	for jogador in range(1, 11):
		
		idade = randint(1, 100)
		altura = randint(150, 200)
		peso = randint(50, 200)

		
		if i == 1:
			somatoriaIdadesTimeUm += idade
		
		if i == 2:
			somatoriaIdadesTimeDois = 0
			somatoriaIdadesTimeDois += idade
		
		if i == 3:
			somatoriaIdadesTimeTres = 0
			somatoriaIdadesTimeTres += idade
			
		if i == 4:
			somatoriaIdadesTimeQuatro = 0 
			somatoriaIdadesTimeQuatro += idade
		
		if i == 5:
			somatoriaIdadesTimeCinco = 0
			somatoriaIdadesTimeCinco += idade	
			
		if idade < 18:
			idadesInferioresDezoito += 1

		if peso > 80:
			pessoasMaioresOitentaQuilos += 1
			
		somaAlturaTodos += altura

