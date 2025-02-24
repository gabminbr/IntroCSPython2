def ordena(lista):
    fim = len(lista)
    for i in range(fim - 1):
        menor_pos = i
        for j in range(i + 1, fim, 1):
            if (lista[j] < lista[menor_pos]):
                menor_pos = j
        aux = lista[i]
        lista[i] = lista[menor_pos]
        lista[menor_pos] = aux
    return lista
