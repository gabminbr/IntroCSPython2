def dimensoes(matriz):
    '''
    (matriz) -> (string formato da matriz)
    recebe como parâmetro uma matriz de n por m e retorna o
    formato dela (ex: 3X2)
    '''
    i = len(matriz)
    j = len(matriz[0])
    formato = str(i) + "X" + str(j)
    print(formato)