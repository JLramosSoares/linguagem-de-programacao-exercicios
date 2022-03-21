# 16) Crie uma função recursiva para descobrir se um número (inteiro não negativo) é primo. A função deve retornar True quando o número for primo e False quando o número não for primo. Teste com 0, 1, 2, 3 e 547.

def primeNumber(n):
    primeNumbers = []
    for i in range(2, n+1):        
        if i % 2 == 0 and i != 2:
            continue
        if i % 3 == 0 and i != 3:
            continue
        if i % 5 == 0 and i != 5:
            continue
        if i % 7 == 0 and i != 7:
            continue
        
        primeNumbers.append(i)
    
    return primeNumbers

primos = primeNumber(500)

print(primos)