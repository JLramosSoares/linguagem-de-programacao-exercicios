"""
Um  time  de basquete  possui  12  jogadores. Faça um programa  que  
preencha  uma matriz  com  o nome  e  a  altura  dos  jogadores,  
e  através de uma função faça os seguintes cálculos:

a) Nome e a altura do jogador mais alto
b) Média da altura do time

Obs: A função deverá receber por parâmetro a matriz e imprimir 
os resultados dentro da função.
"""

from random import randint

mat = []

for i in range(12):
    linha = []
    linha.append(input('Jogador: '))
    linha.append(randint(100,200))
    mat.append(linha)

for linha in mat:
    print(linha)

def jogadorAltoMediaAlturas():
    jogadorAlto = mat[0][1]
    linha = 0
    mediaAltura = 0
    for i in range(12):
        for j in range(2):
            if mat[i][1] > jogadorAlto:
                jogadorAlto = mat[i][1]
                linha = i
            if j == 1:
                mediaAltura += mat[i][j]
    mediaAltura = mediaAltura / 12
    
    print("\nJogador mais alto é {} de altura {}cm".format(mat[linha][0], 
                                                         jogadorAlto))
    
    print("Média das alturas: {}".format(round(mediaAltura, 2)))

jogadorAltoMediaAlturas()