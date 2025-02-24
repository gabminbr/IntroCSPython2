def busca(lista, elemento):
    '''
    (lista, elemento) -> int / bool
    recebe uma lista e um elemento a ser encontrado na lista
    se estiver na lista, retorna o indice, se nao, retorna false
    '''
    for i in range(0, len(lista), 1):
        if (lista[i] == elemento):
            return i
    return False
