# busca alunos cadastrados

lista_alunos = ["João", "Maria", "José", "Ana", "Carlos", "Paula", "Pedro", "Luana", "Mariana", "Fernando"]
nome_elemento = "Ana"  


def busca_alunos(lista, chave):
    for i in range(len(lista)):
        if lista[i] == chave:
            return i
    
    return None

# teste
indice = busca_alunos(lista_alunos, nome_elemento)   
if indice is not None:
    print("O aluno {} está na posição {}".format(nome_elemento, indice))
else:
    print("O aluno {} não está cadastrado".format(nome_elemento))    
