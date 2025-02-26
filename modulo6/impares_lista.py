def encontra_impares(lista, index=0):
    fim = len(lista) - 1
    lista_impares = []
    if(fim == index):
        return eh_impar(lista[index], lista_impares)
    else:
        return eh_impar(lista[index], lista_impares) + encontra_impares(lista, index + 1)
    
def eh_impar(n, lista):
    if(n % 2 != 0):
        lista.append(n)
    return lista
