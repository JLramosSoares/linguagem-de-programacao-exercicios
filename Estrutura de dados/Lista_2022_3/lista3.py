

def selectionSort(array:list) -> None:
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[min] > array[j]:
                min = j
            
        atual = array[i]
        array[i] = array[min] 
        array[min] = atual

def makeList(path:str) -> list:
    with open(path, 'rt') as text:
        words = text.read().split('\n')
        
    return words

def saveList(path:str, array:list) -> None:
    with open(path, 'wt') as save:
        for word in array:
            save.write(word+'\n')
            
def searchWord(word:str, array:list) -> int | None:
    for i in range(len(array)):
        if array[i] == word:
            return i
        
    return None

if __name__ == '__main__':
    #Código da A
    lista = makeList('desordenado.txt')
    print('------Resultado A-------')
    print(lista)
    
    #Código da B
    selectionSort(lista)
    print('\n------Resultado B-------')
    print(lista)
    
    #Código da C
    saveList('ordenado.txt', lista)
    
    #Código da D
    print('\n------Resultado D-------')
    buscaIndice = searchWord('sort', lista)
    print('Índice da palavra \"sort\": ',buscaIndice)
    
    #Código da E
    print('\n------Resultado E-------')