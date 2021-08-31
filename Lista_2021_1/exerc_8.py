from random import randint

timeUmIdades = []
timeDoisIdades = []
timeTresIdades = []
timeQuatroIdades = []
timeCincoIdades = []

somaAlturas = cont = menorQueDezoito = 0

for time in range(1,6):
	
	for i in range(1, 12):
		
		idade = randint(10, 30)
		altura = randint(140, 200)
		peso = randint(50, 90)
		
		if time == 1: 	
			timeUmIdades.append(idade)
			
		if time == 2:
			timeDoisIdades.append(idade)
		
		if time == 3:
			timeTresIdades.append(idade)
		
		if time == 4:
			timeQuatroIdades.append(idade)
		
		if time == 5:
			timeCincoIdades.append(idade)
		
		if peso > 80:
			cont += 1
		
		if idade < 18:
			menorQueDezoito += 1
		
		somaAlturas += altura

mediaIdadesTimeUm = sum(timeUmIdades)/11
mediaIdadesTimeDois = sum(timeDoisIdades)/11
mediaIdadesTimeTres = sum(timeTresIdades)/11
mediaIdadesTimeQuatro = sum(timeQuatroIdades)/11
mediaIdadesTimeCinco = sum(timeCincoIdades)/11						

mediaAlturas = somaAlturas/55

porcentagemMaiorOitenta = cont * 100 / 55 

print("Jogadores menor de 18: {}".format(round(menorQueDezoito, 2)))
print("Média da altura de todos: {}".format(round(mediaAlturas, 2)))
print("Jogadores com mais de 80Kg: {}%".format(round(porcentagemMaiorOitenta, 2)))
print("\nMédia da idade por time:")
print("Time Um: {}".format(round(mediaIdadesTimeUm, 2)))
print("Time Dois: {}".format(round(mediaIdadesTimeDois, 2)))
print("Time Três: {}".format(round(mediaIdadesTimeTres, 2)))
print("Time Quatro: {}".format(round(mediaIdadesTimeQuatro, 2)))
print("Time Cinco: {}".format(round(mediaIdadesTimeCinco, 2)))


