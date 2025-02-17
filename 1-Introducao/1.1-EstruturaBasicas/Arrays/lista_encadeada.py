# Tempo de execução de uma lista encadeada
import time

inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insere_elemento_na_lista(lista, numero):
    novo_no = Node(numero)
    novo_no.next = lista
    return novo_no

def remove_elemento_na_lista(lista):
    lista = lista.next
    return lista    

# teste insere elemento na lista 
numero_posicao = 80

# medir o tempo de execução
start_time = time.perf_counter()
lista_encadeada = insere_elemento_na_lista(inteiros, numero_posicao)
end_time = time.perf_counter()

print(lista_encadeada)
print(f"Tempo de execução ao inserir item da lista: {end_time - start_time} segundos")


#remove elemento na lista 
start_time = time.perf_counter()
lista_encadeada = remove_elemento_na_lista(lista_encadeada)
end_time = time.perf_counter()

print(lista_encadeada)
print(f"Tempo de execução ao remover item da lista: {end_time - start_time} segundos")