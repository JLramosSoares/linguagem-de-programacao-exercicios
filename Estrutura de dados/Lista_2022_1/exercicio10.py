"""
10) Use For ou While para exibir na tela todos números primos existentes no intervalo de 2 a 100.
"""

for i in range(2, 101):
    div = 0
    for j in range(i+1):
        if div > 2:
            break
        if j == 0:
            continue
        if i % j == 0:
            div += 1
            
    if div == 2:
        print(i)