"""
Crie uma função que receba três valores, 'a', 'b' e 'c', que são os 
coeficientes de uma equação do segundo grau e retorne o valor do delta,
que é dado por 'b² -4ac’.
"""

a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = int(input("Valor de C: "))

def delta(a, b, c):
    return b**2 - 4 * a * c

deltaDaEquacao  = delta(a, b, c)

print("\nDelta: "+str(deltaDaEquacao))