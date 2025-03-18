import time
from lista_encadeada import ListaEncadeada

def test_lista_encadeada_remove_elemento():
    lista = ListaEncadeada()

    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # medir o tempo do algoritmo antes de inserir na lista
    start_time = time.perf_counter() 
    
    for numero in numeros:
        lista.insere_elemento_no_inicio(numero)

    print("Lista encadeada após inserções:")
    lista.imprime_result()
    posicao = 6 
    
    end_time = time.perf_counter()
    print()
    print(f"Tempo de execução da inserção: {end_time - start_time:.6f} segundos")
    print()

    # Medir o tempo de execução
    start_time = time.perf_counter()
    lista.remove_elemento_por_posicao(posicao)
    end_time = time.perf_counter()

    print("\nLista encadeada após remoção:")
    lista.imprime_result()
    print()
    print(f"Tempo de execução ao remover item da lista encadeada: {end_time - start_time:.6f} segundos")
    print()

if __name__ == "__main__":
    test_lista_encadeada_remove_elemento()