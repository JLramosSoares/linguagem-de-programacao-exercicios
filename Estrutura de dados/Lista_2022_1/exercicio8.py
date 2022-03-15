"""
8) Use For e a função Range para calcular o Fatorial de 14 (14!). Exiba na tela o resultado.
"""

number = 10
fat = 1
for i in range(number + 1):
    if i == 0:
        continue
    fat *= i

print("!({}) = {}".format(number, fat))