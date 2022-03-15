"""
9) Use While para calcular o Fatorial de 14 (14!). Exiba na tela o resultado.
"""

fat = 1
cont = 1
number = 14
while cont <= number:
    fat *= cont 
    cont+=1

print("!({}) = {}".format(number, fat))