"""
Escreva um programa que armazene em uma matriz, o nome e duas notas de 5 alunos. Calcule e armazene em uma
lista a média de cada aluno e em outra lista o status (media >= 6, “aprovado”, caso contrário, “reprovado”)
faça uma opção para que o usuário possa fazer uma pesquisar por nome. Se encontrar seja exibido na tela:

o posição em que foi encontrado (índice);
o nome do aluno;
o as duas notas e a média;
o status;
"""

from random import randint

matriz = []
status = []
medias = []

for i in range(5):
    linha = [0] * 3
    matriz.append(linha)

for i in range(5):
    for j in range(3):
        if j == 0:
            matriz[i][j] = input("Nome do aluno: ")
        else:
            matriz[i][j] = randint(1, 10)

for linha in matriz:
    print(linha)

for i in range(5):
    total = 0
    for j in range(1, 3):
        if j == 1 or j == 2:
            total += matriz[i][j]
    medias.append(total/2)

for media in medias:
    if media >= 6:
        status.append("Aprovado")
    else:
        status.append("Reprovado")

nome = input("Pesquise um nome: ")

for i in range(5):
    if matriz[i][0] == nome:
        print("\nNome: {}\nÍndice: {}\nNotas: {} e {}\nStatus: {}".format(nome, i, matriz[i][1], matriz[i][2], status[i]))
