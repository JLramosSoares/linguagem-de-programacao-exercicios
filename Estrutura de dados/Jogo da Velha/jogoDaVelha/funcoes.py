
from numpy import ndarray

#Retorna uma lista com caracter de espaço 
def novoJogo(branco:str = ' ') -> list:
    lista = ndarray = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco]
    ]
    
    return lista

#Verificar se uma posição na lista está vazia
def espacoVazio(lista:list, linha:int, col:int) -> bool:
    if lista[linha][col] == ' ':
        return True
    
    return False

#Mostra o estado atual do jogo
def mostrarJogo(lista:list, jogadorAtual:str):
    print("\nVez de:",jogadorAtual)
    print(lista[0])
    print(lista[1])
    print(lista[2])

#Verifica se o espaço está preenchido pelos caracteres 'X' ou 'O'
def espacoPreenchido(lista:list, linha:int, col:int) -> bool:
    if lista[linha][col] == 'X' or lista[linha][col] == 'O':
        return True
    
    return False

#Preenche o espaço de uma lista com sua cordenada e um simbolo 
def preencherEspaco(lista:list, linha:int, col:int, simbolo:str) -> list:
    lista[linha][col] = simbolo

#Verificar se a lista está completamente cheia
def semEspaco(lista:list):
    for linha in range(3):
        for coluna in range(3):
            if espacoVazio(lista, linha, coluna):
                return False

    return True

def ganhou(jogo):
    for i in range(3):
        contLinha = 0
        for j in range(3):
            
            
    