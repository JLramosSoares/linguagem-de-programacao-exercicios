
from jogoDaVelha.funcoes import *

jogo = novoJogo()
vez = True

dadosJogadores = {
    True:{'simbolo':'O', 'jogador':input('Jogador 1: ')},
    False:{'simbolo':'X', 'jogador':input('Jogador 2: ')}
}

while True:
    
    #Pegar os dados do jogador atual através de sua chave (True/False)
    jogadorAtual = dadosJogadores[vez]['jogador']
    simboloAtual = dadosJogadores[vez]['simbolo']
    
    #Mostrar o estado atual do jogo
    mostrarJogo(jogo, jogadorAtual)
    
    #Pegar as coordenadas passadas pelo jogador
    linha = int(input('\nDigite a posição da linha: '))-1
    col = int(input('Digite a posição da coluna: '))-1
    
    #Validar os valores passados
    while (0 > linha or linha > 2) or (0 > col or col > 2):
        mostrarJogo(jogo, jogadorAtual)
        print("\nValor inválido. Por favor, digite valores entre 1 e 3")
        linha = int(input('\nDigite a posição da linha: '))-1
        col = int(input('Digite a posição da coluna: '))-1

    #Verifica se o espaço está preenchido
    while espacoPreenchido(jogo, linha, col):
        mostrarJogo(jogo, jogadorAtual)
        print("\nEspaço já foi preenchido. Digite um espaço válido")
        linha = int(input("\nDigite a posição da linha: "))-1
        col = int(input("Digite a posição da coluna: "))-1
    
    preencherEspaco(jogo, linha, col, simboloAtual)
    
    if semEspaco(jogo):
        mostrarJogo(jogo, jogadorAtual)
        print("\nDeu Velha!")
        break
    
    #Mudar de jogador
    vez = not(vez)


