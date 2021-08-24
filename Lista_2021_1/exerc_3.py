from random import randint

print("A nota do filme deve ser o seguinte: ")
print("1 - Ótimo\n2 - Bom\n1 - Regular")

pessoas = somaIdade = 0
qtndRegular = qtndBom = qtndOtimo = 0 
 
idade = int(input("\nIdade: "))

while idade > 0 :
	
	nota = randint(1,3)
	
	if nota == 1:
		qtndRegular += 1
		
	if nota == 2:
		qtndBom += 1
		
	if nota == 3:
		qtndOtimo += 1
	
	pessoas += 1
	somaIdade += idade
		
	idade = int(input("Idade: "))


mediaIdades = somaIdade/pessoas

print("\nTotal Ótimo: {}".format(qtndOtimo))
print("Total Regular: {}".format(qtndRegular))
print("Total Bom: {}".format(qtndBom))
print("Média Idades: {}".format(mediaIdades))
