"""
4) Escreva um programa que atenda aos seguintes requisitos:
• Atribuir à variável chamada meuId, o número seu RA (registro de aluno). Não use função
de entrada, apenas digite diretamente o RA.
• Verificar se meuId é par, em caso positivo, exibir na tela "É Par",
caso contrário, exiba "É Impar".
"""

meuId = 1310482132001
if meuId % 2 == 0:
    print("É Par")
else:
    print("É Impar")