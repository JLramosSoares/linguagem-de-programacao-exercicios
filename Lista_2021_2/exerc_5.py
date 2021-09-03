"""
Faça um programa que preencha uma lista com os nomes de 5 produtos, e 
outra lista com o valor dos produtos. Calcule e mostre:

a. a quantidade de produtos que o valor é abaixo de 10 reais;
b. a média dos valores dos produtos;
c. a quantidade de produtos que valor acima da média;
d. a maior valor e o nome do produto;
e. faça uma listagem que imprima na tela (Nome Vlr do produto)
"""

produtos = []
valores = []

for i in range(5):
    produtos.append(input("\nNome do produto: "))
    valores.append(float(input("Valor do produto: R$")))

mediaValores = sum(valores)/len(valores)
acimaDaMedia = 0

for i in range(5):
    
    if valores[i] > mediaValores: 
        acimaDaMedia += 1

indiceMaiorValor = valores.index(max(valores))

print("\nQuantidade de produtos: {}".format(len(produtos)))
print("Média dos valores: R${}".format(mediaValores))
print("Quantidade de valores acima da média: {}".format(acimaDaMedia))
print("Produto de maior valor e o nome: {} - R${}".format(produtos[indiceMaiorValor],
                                                        max(valores)))


