"""
5) Construa um dicionário dictCartaValor para associar o valor
correspondente de cada carta do jogo de truco. Considere as
seguintes informações:

• Use como chave os elementos contidos no conjunto
baralhoTruco.

• Tradicionalmente, usa-se a ordem Dama-Valete-Rei no jogo,
assim, cartas numéricas de 4 a 7 assumem seu próprio valor e
outras cartas, assumem:

• Q(Dama)=8, J(Valete)=9, K(Rei)=10,
A(Ás)=11, 2(Dois)=12, 3(Três)=13.

• Em algumas situações do jogo, os naipes influenciam, dessa
forma, no valor de cada carta deve ser somado:
• 0.3 para paus (♣),
• 0.2 para copas (♥),
• 0.1 para espadas (♠), e
• 0.0 para ouro (♦).

• Assim, durante uma partida as cartas poderão ter os valores
comparados considerando apenas a parte inteira, ou quando for
conveniente, pode-se considerar o valor todo.
"""

baralhoTruco = { 'A♦', 'A♠', 'A♥', 'A♣', '2♦', '2♠', '2♥', '2♣',
'3♦', '3♠', '3♥', '3♣', '4♦', '4♠', '4♥', '4♣', '5♦', '5♠', '5♥', '5♣',
'6♦', '6♠', '6♥', '6♣', '7♦', '7♠', '7♥', '7♣', 'J♦', 'J♠', 'J♥', 'J♣',
'Q♦', 'Q♠', 'Q♥', 'Q♣', 'K♦', 'K♠', 'K♥', 'K♣' }

valCarta = { '4': 4, '5': 5, '6': 6, '7': 7, 'Q': 8, 'J': 9, 'K': 10, 'A': 11,'2': 12, '3': 13 }

valNaipe = { '♦':0.0, '♠':0.1, '♥':0.2, '♣':0.3 }

dictCartaValor = dict()

for carta in baralhoTruco:
    valor = valCarta[carta[0]] + valNaipe[carta[1]]
    dictCartaValor[carta] = valor

print(dictCartaValor)