# busca de moedas cadastradas

lista_moedas =["real", "dolar", "euro", "libra", "peso", "iene", "franco", "coroa", "rublo", "rupia","yang", "dinar", "shekel", "baht", "dong", "florim", "guarani", "kuna", "lira", "mark","peseta", "rand"
]   

#input
moeda = input("Digite o nome da moeda que deseja procurar: ")
print("Moeda digita:", moeda)


def busca_moedas(lista, nome_moeda):
    for i in range(len(lista)):
        if lista[i] == nome_moeda:
            return i
    return None

#teste
indice = busca_moedas(lista_moedas, moeda) 

if indice is not None:
    print("A moeda {} está na posição {}".format(moeda, indice))
else:
    print("A moeda {} não está cadastradada".format(moeda))    
