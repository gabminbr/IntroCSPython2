def conta_letras(frase, contar="vogais"):
    qtd = 0
    frase = frase.lower()
    vogais = ['a', 'e', 'i', 'o', 'u']
    if (contar == "vogais"):
        for i in range(0, len(frase), 1):
            if (frase[i] in vogais):
                qtd += 1
    if (contar == "consoantes"):
        for i in range(0, len(frase), 1):
            if (frase[i] not in vogais and frase[i] != " "):
                qtd += 1
    return qtd
