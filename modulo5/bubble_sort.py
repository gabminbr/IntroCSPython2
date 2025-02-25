def bubble_sort(lista):
    length = len(lista)
    for i in range(0, length - 1, 1):
        for j in range(0, length - i - 1, 1):
            if (lista[j] > lista[j + 1]):
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
                print(lista)
    return lista