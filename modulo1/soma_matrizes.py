def soma_matrizes(m1, m2):
    i1 = len(m1)
    j1 = len(m1[0])
    i2 = len(m2)
    j2 = len(m2[0])

    if (i1 == i2 and j1 == j2):
        matriz_somada = []
        for i in range(0, len(m1), 1):
            linha = []
            for j in range(0, len(m1[i]), 1):
                linha.append(m1[i][j] + m2[i][j])
            matriz_somada.append(linha)
        
        return matriz_somada
    
    return False
