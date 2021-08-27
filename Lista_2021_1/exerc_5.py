numeros = []

for i in range(10):
	
	numeros.append(int(input("Digite um número: ")))

for numero in numeros:
	
	fat = 1
	for i in range(2, numero + 1):
		fatorial = fat = fat * i
		
	print("\n!({}) = {}".format(numero, fatorial))
