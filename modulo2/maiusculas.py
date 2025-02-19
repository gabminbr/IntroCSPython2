def maiusculas(frase):
    '''
    (string) -> (string)
    recebe uma string como parametro e devolve
    uma outra string apenas com as maiusculas
    que apareceram na string original
    '''
    # 65 - 90
    string_maiuscula = ""
    for i in range(0, len(frase), 1):
        if (ord(frase[i]) >= 65 and ord(frase[i]) <= 90):
            string_maiuscula += frase[i]
    
    return string_maiuscula
