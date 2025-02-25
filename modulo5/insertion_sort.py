def insertion_sort(lista):
    sorted_lista = [lista[0]]
    for i in range(1, len(lista), 1):
        index = 0
        for j in range(len(sorted_lista)):
            if(lista[i] >= sorted_lista[j]):
                index += 1
            else:
                break
        sorted_lista.insert(index, lista[i])
    return sorted_lista