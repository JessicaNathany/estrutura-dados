# Busca linear em lista em alocação sequencial

def  busca(lista, elemento):
    """Retorna o índice do elemento se ele estiver na lista, ou None caso contrário"""
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i

    return None

# teste
lista_estranha = [8,"5", 32, 0, "python", 11]  
elemento = 32

indice = busca(lista_estranha, elemento)
if indice is not None:
    print("O índice do elemento {} é {}".format(elemento, indice))
else:
    print("O elemento {} não se encontra na lista".format(elemento))    