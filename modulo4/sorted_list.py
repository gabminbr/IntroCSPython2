def ordenada(lista):
    '''
    (lista) -> (bool)
    recebe uma lista como parâmetro e retorna
    True se estiver ordenada, False se não
    '''
    for i in range(0, len(lista) - 1, 1):
        menor_element = i
        for j in range(i + 1, len(lista), 1):
            if (lista[menor_element] > lista[j]):
                return False
    return True
