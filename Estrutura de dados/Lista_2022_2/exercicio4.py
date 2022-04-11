"""
4) Construa um conjunto (SET) chamado baralhoTruco contendo apenas
as cartas usadas no jogo de truco. Use os elementos preexistentes
na lista baralho54cartas.

Elimine as cartas desnecessárias: cartas que começam com 8, 9, 10
e os curingas(joker).
"""

baralho54cartas = ['A♦', 'A♠', 'A♥', 'A♣', '2♦', '2♠', '2♥', '2♣',
'3♦', '3♠', '3♥', '3♣', '4♦', '4♠', '4♥', '4♣', '5♦', '5♠', '5♥','5♣','6♦', '6♠', '6♥', '6♣', '7♦', '7♠', '7♥', '7♣', '8♦', '8♠', '8♥', '8♣','9♦', '9♠', '9♥', '9♣', '10♦', '10♠', '10♥', '10♣','J♦', 'J♠', 'J♥', 'J♣','Q♦', 'Q♠', 'Q♥', 'Q♣', 'K♦', 'K♠', 'K♥', 'K♣', chr(127167), chr(127183)]

baralhoTruco = set()
conjuntoCartas = []

#Organiza em uma lista um conjunto de quatro cartas excluindo as cartas coringas
limit=0
while limit <= 50:
    conjuntoCartas.append(baralho54cartas[limit:limit+4])
    limit += 4

"""
Percorre a matriz pulando o conjunto 7, 8 e 9. Ignora o conjunto de 
cartas 8, 9, 10 e adiciona as demais no set.
"""
for i in range(len(conjuntoCartas)):
    if (i == 7) or (i == 8) or (i == 9):
        pass
    else:
        for j in range(len(conjuntoCartas[i])):
            baralhoTruco.add(conjuntoCartas[i][j])
        
#Exibe o conjunto das cartas de truco
print(baralhoTruco)