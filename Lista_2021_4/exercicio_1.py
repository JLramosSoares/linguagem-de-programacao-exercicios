"""
Crie  uma  função  que  receba  1  número  inteiro  como  parâmetro
e  verifique  se  ele  é perfeito, ou seja, se a soma dos seus
divisores exceto ele mesmo dá o próprio número, a mensagem se o 
número é perfeito ou não deve ser mostrada no programa principal.
"""

num = int(input("Digite um número: "))

def numeroPerfeito(num):
    somaDivisores = 0
    for i in range(1, num):
        if num % i == 0:
            somaDivisores += i
    
    if somaDivisores == num:
        print("\nO número {} é um inteiro.".format(num))
        print("Soma dos Divisores: {}".format(somaDivisores))
    else:
        print("\nO número {} NÃO É um inteiro.".format(num))
        print("Soma dos Divisores: {}".format(somaDivisores))

numeroPerfeito(num)

