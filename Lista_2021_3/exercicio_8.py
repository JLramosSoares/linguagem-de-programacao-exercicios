"""
Escreva um programa que preencha uma lista com os nomes de 10 alunos,
e outra lista com a média dos alunos. Calcule e mostre:
a) a média da classe;
b) a quantidade de alunos que tiveram média igual ou superior a 7;
c) a quantidade de alunos que tiveram média abaixo de 7;
d) a maior média da classe e nome do aluno que obteve a maior média
"""

from random import randint

alunos = []
medias = []

aprovados = reprovados = 0

for i in range(4):
    alunos.append(input("Nome do aluno: "))
    medias.append(randint(0, 10))

mediaClasse = sum(medias)/len(alunos)

for i in range(len(alunos)):

    if i == 0:
        maiorMedia = medias[i]
        indiceMaiorMedia = i

    if maiorMedia < medias[i]:
        maiorMedia = medias[i]
        indiceMaiorMedia = medias.index(medias[i])

    if medias[i] >= 7:
        aprovados += 1
    if medias[i] < 7:
        reprovados += 1

print("\nMédia da classe: {}\nAprovados: {}\nReprovados: {}".format(mediaClasse,
                                                                 aprovados,
                                                                 reprovados))

print("\nAluno de maior média: {}\nMaior Média: {}".format(alunos[indiceMaiorMedia], maiorMedia))