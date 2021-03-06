

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

def binarySearch(word:str, array:list, i=0, j=None) -> int:
    if j == None: j = len(array)-1
    if i <= j:
        central = (i+j) // 2
        if array[central] == word:
            return central
        elif array[central] < word:
            return binarySearch(word, array, central+1, j)
        else:
            return binarySearch(word, array, i, central-1)

if __name__ == '__main__':
    #Código da A
    lista = makeList('Arquivos TXT/desordenado.txt')
    print('------Resultado A-------')
    print(lista)
    
    #Código da B
    selectionSort(lista)
    print('\n------Resultado B-------')
    print(lista)
    
    #Código da C
    saveList('Arquivos TXT/ordenado.txt', lista)
    
    #Código da D
    print('\n------Resultado D-------')
    buscaIndice = searchWord('sort', lista)
    print('Índice da palavra \"sort\": ',buscaIndice)
    
    #Código da E
    print('\n------Resultado E-------')
    buscaIndice = binarySearch('sort', lista)
    print('Índice da palavra \"sort\": ',buscaIndice)