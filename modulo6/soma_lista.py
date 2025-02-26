def soma_lista(lista, index=0):
    fim_lista = len(lista) - 1
    if(index == fim_lista):
        return lista[index]
    else:
        return lista[index] + soma_lista(lista, index + 1)
