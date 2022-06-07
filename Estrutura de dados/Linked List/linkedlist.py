from typing import Any

class No:
    def __init__(self, p_dado:Any = None, p_prox=None) -> None:
        self.dado: Any #Pode ser qualquer dado
        self.prox: No  #O prox recebe um Node
    
        self.dado = p_dado
        self.prox = p_prox
        
class LinkedList:
    def __init__(self, *p_dados) -> None:
        self.topo: No
        
        self.topo = None
        for dado in p_dados:
            self.inserir_ini(dado)

    def inserir_ini(self, p_dado=None):
        if self.topo is None:
            self.topo = No(p_dado)
        else:
            aux = self.topo
            self.topo = No(p_dado)
            self.topo.prox = aux
            
    def mostrar_str(self, no:No = None):
        if self.topo is None:
            return None
        
        if no is None:
            no = self.topo 
        
        if no.prox is None:
            return repr(no.dado)
         
        return repr(no.dado) +' -> '+self.mostrar_str(no.prox)

    def contar(self, no:No=None, cont:int=0):
        if self.topo is None:
            return None
    
        if self.prox is None:
            return cont
        
        else:
            cont += 1
            return self.contar(self.prox, cont)
        
        # contador = 1
        # no = self.topo
        # while True:
        #     if no.prox is None:
        #         return contador
        #     else:
        #         contador += 1
        #         no = no.prox

lista = LinkedList(1, 2, 4)
print(lista.contar())