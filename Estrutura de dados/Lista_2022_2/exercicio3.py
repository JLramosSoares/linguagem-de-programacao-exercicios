"""
3) Faça um código para que a lista baralho54Cartas contenha todos
elementos de baralho52Cartas juntamente com os elementos da
variável jokers. (Altere apenas o valor de baralho54Cartas, não
altere o valor de baralho52Cartas nem de jokers)
"""


jokers = (chr(127167), chr(127183))
baralho52Cartas = ['A♦', 'A♠', 'A♥', 'A♣', '2♦', '2♠', '2♥', '2♣',
'3♦', '3♠', '3♥', '3♣', '4♦', '4♠', '4♥', '4♣', '5♦', '5♠', '5♥', '5♣',
'6♦', '6♠', '6♥', '6♣', '7♦', '7♠', '7♥', '7♣', '8♦', '8♠', '8♥', '8♣',
'9♦', '9♠', '9♥', '9♣', '10♦', '10♠', '10♥', '10♣', 'J♦', 'J♠', 'J♥', 'J♣',
'Q♦', 'Q♠', 'Q♥', 'Q♣', 'K♦', 'K♠', 'K♥', 'K♣']

#Faz um cópia dos valores do baralho52cartas
baralho54Cartas = baralho52Cartas[:]

#Adiciona as cartas coringas no baralho54cartas
baralho54Cartas.append(jokers[0])
baralho54Cartas.append(jokers[1])

print(baralho52Cartas)
print()
print(baralho54Cartas)