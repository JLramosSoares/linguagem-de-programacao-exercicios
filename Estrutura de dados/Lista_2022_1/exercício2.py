"""
2) Escreva um programa que atenda aos seguintes requisitos:
• Armazenar em uma variável chamada meuDado, um dado qualquer informado pelo usuário.
Deverá aparecer a seguinte mensagem "Digite um dado qualquer e tecle [Enter]:".
• Exibir na tela o conteúdo da variável meuDado.
• Exibir na tela o tipo (type) de dado da variável meuDado.
• Exibir na tela o endereço (id) que a variável meuDado ocupa.
"""

meuDado = input("Digite um dado qualquer e tecle [Enter]: ")
print("\nConteúdo da Variável: {}\nTipo: {}\nID da variável: {}".format(meuDado, type(meuDado), id(meuDado)))
