"""
Escreva uma função que receba como parâmetro uma lista com 10 nomes
e um nome para pesquisa. Essa função deverá realizar uma busca do nome
na lista, retornando TRUE se encontrar ou FALSE se não encontrar.
"""

nomes = []

for i in range(10):
    nomes.append(input("Nome: "))

def buscaNome(nomes, nome):
    if nome in nomes:
        return True
    else:
        return False

print(buscaNome(nomes, 'João'))