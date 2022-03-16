""" 
5) Escreva um programa que atenda aos seguintes requisitos do zoológico de PythonCity:
---------------------------------------------------------------
• Receber a idade, o gênero do visitante [M/F] e se o visitante é estudante [S/N].
O zoológico de PythonCity decidiu fazer a seguinte promoção:
---------------------------------------------------------------
• O preço integral do ingresso (sem descontos) é de R$ 40,00
• Criança com 6 anos ou menos não paga. 
• Pessoa com 65 anos ou mais paga 1 real (preço simbólico).
• Estudante paga meia entrada.
• Descontos de 25% para o gênero feminino:
• Estudante do gênero feminino paga a meia entrada com um desconto de 25%.
• Pessoa não-estudante do gênero feminino paga a entrada integral com um desconto de
25%.
• Pessoa com 65 anos ou mais paga o preço simbólico com um desconto de 25%.
------------------------------------------------------------------
• A pessoa deve ser beneficiada com o melhor caso, ou seja, se for estudante e também
tiver mais de 65 anos, deverá pagar o preço simbólico, sofrendo também o desconto de
gênero, se for o caso.
• Não será concedido desconto em qualquer outro caso não previsto.
-------------------------------------------------------------------
• Calcule o preço a pagar.
• Calcule o desconto total concedido (Preço integral menos o Preço a pagar).
• Exiba na tela o preço a pagar.
• Exiba na tela o desconto total concedido.
"""

#Recebe a idade o genêro e se é estudante
idade = int(input("Idade: "))
genero = input("Genêro [M/F]: ")
estudante = input("Estudante [S/N]: ")
valor = 40
desconto = 0

if idade <= 6:
    valor = 0
    desconto = 40
else:
    if idade >= 65:
        valor = 1
        desconto = 39
    if genero == 'F':
        valor = valor - (valor * 0.25)
        desconto = desconto - valor
    if estudante == 'S':
        valor = (valor / 2)




print(valor)