class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEncadeada:
    def  __init__(self):
        self.head = None # inicializa a lista encadeada sem nenhum nó

    def insere_elemento_no_inicio(self, data):
            
            # insere um elemento em uma lista encadeada
            novo_no = Node(data)
            novo_no.next = self.head 
            self.head = novo_no

    def remove_elemento_por_posicao(self, posicao):
            
            if self.head == None:
                print("Lista vazia")
                return
            
            if posicao == 0:
                self.head = self.head.next
                return
            
            atual = self.head
            anterior = None
            contator = 0       
            
            while atual is not None and contador < posicao:
                anterior = atual
                atual = atual.next
                contador += 1
                
            if atual is None:
                print("Posição inválida")
                return
            
    def imprime_result(self):
        atual = self.head
        
        while atual is not None:
            print(f"posicao atual", atual.data)
            atual = atual.next
        print("None")
            