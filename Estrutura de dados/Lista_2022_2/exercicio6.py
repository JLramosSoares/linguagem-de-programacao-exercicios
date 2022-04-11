"""
6.a) Descreva em linhas gerais para que serve o código contido no
for (linha13 à linha19).

É um laço de repetição usado para distribuir três cartas aleatóriamente para dois
jogadores usando o conjunto de cartas pré-existente da variável meuBaralho, e remover a carta sorteada do conjunto para que ela não possa ser sorteada novamente para outro jogador. Também determina a carta que será sorteada para ser posta na mesa, ou tombada. 
---------------------------------------------------------------------------------
6.b) O que faz o segundo parâmetro da função random.sample (ou
seja, o que faz o número 1 que aparece nas linhas: 14, 17 e 21)

O segundo parâmetro da função serve para determinar a quantidade de valores que será sorteado do conjunto meuBaralho. 
---------------------------------------------------------------------------------
6.c) O que faz o número zero entre colchetes [0] (nas linhas: 14, 17
e 21), por que é necessário usá-lo?

É necessário usá-lo, pois o tipo de dado que a função .sample() retorna é uma lista. E a função .add() não aceita esse tipo de dado, sendo necessário colocar apenas o valor, utilizando o index 0 para acessar o elemento.    
---------------------------------------------------------------------------------
Obs. Entregue as respostas do exercício 6 também usando um arquivo
.py (exe_06.py), de forma a facilitar a correção pelo professor no
mesmo ambiente.
"""