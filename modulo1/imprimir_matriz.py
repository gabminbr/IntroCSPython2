def imprime_matriz(matriz):
    '''
    (matriz) -> imprime a matriz de forma visual
    '''
    for i in range(0, len(matriz), 1):
        for j in range(0, len(matriz[i]), 1):
            print(matriz[i][j], end = "")
            if(j != len(matriz[i]) - 1):
                print(" ", end = "")
            else:
                print("", end = "")
        print()

matriz = [[1,2,3],[4,5,6],[7,8,9]]
imprime_matriz(matriz)