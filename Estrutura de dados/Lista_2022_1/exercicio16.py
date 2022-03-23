# 16) Crie uma função recursiva para descobrir se um número (inteiro não negativo) é primo. A função deve retornar True quando o número for primo e False quando o número não for primo. Teste com 0, 1, 2, 3 e 547.


def primeNumber(num:int, i:int = 2) -> bool:
    if num == 0 or num == 1:
        return False
    if(num == i):
        return True
    if(num % i == 0):
        return False
    
    return primeNumber(num, i+1)

print(primeNumber(0))
print(primeNumber(1))
print(primeNumber(2))
print(primeNumber(3))
print(primeNumber(547))