# Nome: José Victor Goulart dos Santos
# Matrícula: 20200412
matriz = []
diagonalP1 = 0
diagonalP2 = 0
diagonalInvP1 = 0
diagonalInvP2 = 0
horizontalP1 = 0
horizontalP2 = 0
verticalP1 = 0
verticalP2 = 0
highestP1 = 0
highestP2 = 0
firstPos = 0
while True:
    print("1 - Preencher o tabuleiro lendo valores do teclado")
    print("2 - Preencher o tabuleiro randomicamente")
    print("3 - Encerrar o programa")
    option = int(input("Digite o número para uma das opções acima: "))

    if(option == 1):
        
        for i in range(4):
            matriz.append([int(x) for x in input().split()])
        # Verifica a repetição de elemento na matriz
        for j in range(4):
            for k in range(4):
                if(matriz[j][k] == 1):
                    count = 0
                    # Verifica se tem cinco elementos 1 repetidos na horizontal
                    if(4 - k >= 3):
                        for l in range(4 - k):
                            if(matriz[j][k + l] == 1):
                                count += 1
                                if(count >= horizontalP1):
                                    horizontalP1 = count
                            else:
                                count = 0
                    # Verifica se tem cinco elementos 1 repetidos na vertical
                    count = 0
                    if(4 - j >= 3):
                        for c in range(4 - j):
                            if(matriz[j + c][k] == 1):
                                count += 1
                                if(count >= verticalP1):
                                    verticalP1 = count
                            else:
                                count = 0

                    # Verifica se tem cinco elementos 1 repetidos na diagonal principal
                    count = 0
                    # print(k)
                    # print(j)
                    for dp in range(4 - k):
                        if(j + dp < 4):
                            if(matriz[j + dp][k + dp] == 1):
                                count += 1
                                if(count >= diagonalP1):
                                    diagonalP1 = count
                            else:
                                count = 0

                    # Verifica se tem cinco elementos 1 repetidos na diagonal inversa        
                    for di in range(4 - k):
                        if(matriz[j - di][k - di] == 1):
                            count += 1
                            if(count >= diagonalInvP1):
                                diagonalInvP1 = count
                        else:
                            count = 0

                if(matriz[j][k] == 2):
                    count = 0
                    # Verifica se tem cinco elementos 2 repetidos na horizontal
                    if(4 - k >= 3):
                        for l in range(4 - k):
                            if(matriz[j][k + l] == 2):
                                count += 1
                                if(count >= horizontalP2):
                                    horizontalP2 = count
                            else:
                                count = 0
                    # Verifica se tem cinco elementos 2 repetidos na vertical
                    if(4 - k >= 3):
                        count = 0
                        for c in range(4 - j):
                            if(matriz[j + c][k] == 2):
                                count += 1
                                if(count >= verticalP2):
                                    verticalP2 = count
                            else:
                                count = 0

    # elif(option == 2):
    elif(option == 3):
        break
    print(horizontalP1)
    print(verticalP1)
    # print(diagonalP1)
    # print(diagonalInvP1)
    print(horizontalP2)
    print(verticalP2)
    # print(diagonalP2)
    # print(diagonalInvP2)
    print(matriz)
