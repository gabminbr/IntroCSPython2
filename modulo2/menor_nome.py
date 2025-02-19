def menor_nome(nomes):
    menor_string = nomes[0].capitalize().strip()
    for i in range(1, len(nomes), 1):
        nome_atual = nomes[i].capitalize().strip()
        if (len(menor_string) > len(nome_atual)):
            menor_string = nome_atual
    return menor_string