def primeiro_lex(lista):
    primeiro = lista[0]
    for i in range(1, len(lista), 1):
        if (lista[i] < primeiro):
            primeiro = lista[i]

    return primeiro
