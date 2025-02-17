# Tempo de execução de uma lista linear
import time

inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def insere_numero_no_meio(lista, numero):
    lista.insert(5, numero)
    return lista

def remove_numero_no_meio(lista):
    lista.pop(5)
    return lista 


# teste insere elemento na lista    
numero_para_inserir = 80

# medir o tempo de execução
start_time = time.perf_counter()
lista_sequencial = insere_numero_no_meio(inteiros, numero_para_inserir)
end_time = time.perf_counter()

print(lista_sequencial)
print(f"Tempo de execução ao inserir item da lista: {end_time - start_time} segundos")

#remove elemento na lista 
start_time = time.perf_counter()
lista_sequencial = remove_numero_no_meio(lista_sequencial)
end_time = time.perf_counter()

print(lista_sequencial)
print(f"Tempo de execução ao remover item da lista: {end_time - start_time} segundos")
