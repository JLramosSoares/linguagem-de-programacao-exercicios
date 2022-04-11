"""
2) Escreva um código Python para combinar cada elemento da
variável cartas com cada elemento da variável naipes, formando
assim, os elementos de uma lista chamada baralho52Cartas:
"""

cartas = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

naipes = ('\u2666', '\u2660','\u2665','\u2663')

baralho52cartas = []

for carta in cartas:
    for naipe in naipes:
        baralho52cartas.append(carta+naipe)

print(baralho52cartas)