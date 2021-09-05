"""
Escreva um programa que preencha uma lista com os nomes de 5 vendedores,
preencha também outra lista com valor total das vendas de cada vendedor.
Cada vendedor recebe 10% de comissão sobre as vendas. 
Faça os seguintes cálculos e mostre os resultados na tela:

a. Uma listagem com o nome e o valor a receber de cada vendedor 
(total das vendas * 0.10)
b. O total (bruto) vendido pelos 5 vendedores
c. A média do total de vendas (valor bruto vendido por cada vendedor)
d. A quantidade de vendedores que venderam acima da média das vendas
e. O maior valor de comissão e o nome do vendedor que recebeu
"""

from random import randint

vendedores = []
valorTotalVendas = []

for i in range(5):
    vendedores.append(input("Nome do vendedor: "))
    valorTotalVendas.append(randint(50, 1000))

print("="*45)

for i in range(5):
    comissao = valorTotalVendas[i] * 0.1
    print("O {} deverá receber R${}".format(vendedores[i],
                                            round(comissao, 2)))
print("="*45)
for i in range(5):
    print("\nVendedor: {}".format(vendedores[i]))
    print("Total Bruto: R${}".format(valorTotalVendas[i]))

print("="*45)

mediaTotalVendas = sum(valorTotalVendas)/len(valorTotalVendas)
acimaMedia = 0

for i in range(len(valorTotalVendas)):
    if valorTotalVendas[i] > mediaTotalVendas:
        acimaMedia += 1

indiceMaiorValor = valorTotalVendas.index(max(valorTotalVendas))

print("Média de vendas: {}".format(mediaTotalVendas))
print("Quantidade de vendedores acima da média: {}".format(acimaMedia))
print("A comissão mais alta vai para {} no valor de R${}".format(vendedores[indiceMaiorValor],
                                                                round(valorTotalVendas[i]*0.1, 2)))

