"""
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
coletando dados sobre o salário, idade e o número de filhos.
Escreva um programa que leia esses dados, por exemplo para 10 pessoas.
Armazene esses dados em uma matriz, depois calcule e mostre:

a) A média de salário da população
b) A média do número de filhos
c) A quantidade de filhos das pessoas que tem idade entre 15 a 25 anos
d) A média de salário de pessoas que tem idade entre 20 a 30 anos
"""

from random import randint

mat = []

for i in range(10):
    mat.append([0]*3)

for i in range(10):
    for j in range(3):
        if j == 0:
            mat[i][j] = randint(800, 5000)
        if j == 1:
            mat[i][j] = randint(20, 40)
        if j == 2:
            mat[i][j] = randint(0, 5)

cont = mediaSalarios = mediaFilhos = qtndFilhos = mediaSalarioVinteTrinta = 0

for i in range(10):
    for j in range(3):
        if j == 0:
            mediaSalarios += mat[i][j]

        if j == 2:
            mediaFilhos += mat[i][j] 

        if j == 1:

            if 15 < mat[i][j] < 25:
                qtndFilhos += mat[i][2]
            
            if 20 < mat[i][j] < 30:
                mediaSalarioVinteTrinta += mat[i][0]
                cont += 1

mediaSalarios = mediaSalarios/10
mediaFilhos = mediaFilhos/10
mediaSalarioVinteTrinta = mediaSalarioVinteTrinta/cont

for linha in mat:
    print(linha)

print("\nA média dos salários: {}\nMédia Filhos: {}".format(mediaSalarios, mediaFilhos))
print("A quantidade de filhos de pesssoas entre 15 e 25: ",qtndFilhos)
print("Média de salário de pessoas entre 20 e 30: ",mediaSalarioVinteTrinta)
