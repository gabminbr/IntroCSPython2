def busca(lista, elemento):
    primeiro = 0
    fim = len(lista) - 1

    while(primeiro <= fim):
        meio = (fim + primeiro) // 2
        print(meio)
        if (lista[meio] == elemento):
            return meio
        else:
            if(elemento < lista[meio]):
                fim = meio - 1
            else:
                primeiro = meio + 1
    return False
