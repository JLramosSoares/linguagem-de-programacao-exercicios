# 16) Crie uma função recursiva para descobrir se um número (inteiro não negativo) é primo. A função deve retornar True quando o número for primo e False quando o número não for primo. Teste com 0, 1, 2, 3 e 547.

def primeNumber(n:int) -> bool:
    if n == 0:
        return False
    else:
        div = 0
        if n % primeNumber(n - 1) == 0:
            div += 1
        if div == 2:
            return True
        
primeNumber(10)