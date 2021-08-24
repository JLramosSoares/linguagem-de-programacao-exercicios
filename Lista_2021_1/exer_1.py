

for i in range(1, 11):
	number = int(input("Digite um número: "))
	
	if i == 1: 
		menor = number
		soma_pares = qtnd_impares = soma_maiorvinte = qtnd_maiorvinte = 0
	
	if number < menor: 
		menor = number 
	
	if (number % 2 == 0) and (number > 10):
		soma_pares += number
	
	if number % 2 != 0:
		qtnd_impares += 1

	if number > 20: 
		soma_maiorvinte += number
		qtnd_maiorvinte += 1
		
print("\nMenor: {}".format(menor))
print("A soma dos pares maiores que 10: {}".format(soma_pares))
print("A quantidade de ímpares: {}".format(qtnd_impares))
		
if qtnd_maiorvinte > 0: 
	media_maiorvinte = soma_maiorvinte / qtnd_maiorvinte
	print("A média dos números maiores que 20: {}".format(media_maiorvinte)) 


		
	
