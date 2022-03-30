#11) Exibir na tela os primeiros 100 números primos.

#Contar os números primos que aparecerem
contPrimeNumber = 0
#O número para ser verificado
num = 2

while contPrimeNumber <= 99:
    div = 0
    for i in range(1, num+1):
        if num % i == 0:
            div += 1
    if div == 2:
        contPrimeNumber += 1
        print("Primo: {} - Posição: {}".format(num, contPrimeNumber))
    
    num += 1
       
    