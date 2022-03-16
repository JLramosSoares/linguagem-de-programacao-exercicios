# 15) Crie uma função recursiva para calcular o fatorial de n. Teste 14! (n=14)

def fatorial(n:int) -> int:
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

number = 14

print("!({}) = {}".format(number, fatorial(number)))    
