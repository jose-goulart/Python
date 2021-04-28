# Nome: José Victor Goulart dos Santos
# Matrícula: 20200412
from random import randint

while True:
    print("1 - Preencher o tabuleiro lendo valores do teclado")
    print("2 - Preencher o tabuleiro randomicamente")
    print("3 - Encerrar o programa")
    option = int(input("Digite o número para uma das opções acima: "))

    if(option == 1):
        matriz = []
        winP1 = 0
        winP2 = 0

        for i in range(10):
            matriz.append([int(x) for x in input().split()])
        # Verifica a repetição de elemento na matriz
        for j in range(10):
            for k in range(10):
                if(matriz[j][k] == 1):
                    count = 0
                    # Verifica se tem cinco elementos 1 repetidos na horizontal
                    if(10 - k >= 5):
                        for l in range(10 - k):
                            if(matriz[j][k + l] == 1):
                                count += 1
                                if(count >= 5):
                                    winP1 = 1
                            else:
                                count = 0
                    # Verifica se tem cinco elementos 1 repetidos na vertical
                    count = 0
                    if(10 - j >= 5):
                        for c in range(10 - j):
                            if(matriz[j + c][k] == 1):
                                count += 1
                                if(count >= 5):
                                    winP1 = 1
                            else:
                                count = 0

                    # Verifica se tem cinco elementos 1 repetidos na diagonal principal
                    count = 0
                    # print(k)
                    # print(j)
                    if(10 - k >= 5):
                        for dp in range(10 - k):
                            if(j + dp < 10):
                                if(matriz[j + dp][k + dp] == 1):
                                    count += 1
                                    if(count >= 5):
                                        winP1 = 1
                                else:
                                    count = 0

                    # Verifica se tem cinco elementos 1 repetidos na diagonal inversa
                    count = 0
                    # if(k + 1 >= 5):
                    for di in range(k + 1):
                        if(j + di < 10):
                            if(matriz[j + di][k - di] == 1):
                                count += 1
                                if(count >= 5):
                                    winP1 = 1
                            else:
                                count = 0

                if(matriz[j][k] == 2):
                    count = 0
                    # Verifica se tem cinco elementos 1 repetidos na horizontal
                    if(10 - k >= 5):
                        for l in range(10 - k):
                            if(matriz[j][k + l] == 2):
                                count += 1
                                if(count >= 5):
                                    winP2 = 1
                            else:
                                count = 0
                    # Verifica se tem cinco elementos 1 repetidos na vertical
                    count = 0
                    if(10 - j >= 5):
                        for c in range(10 - j):
                            if(matriz[j + c][k] == 2):
                                count += 1
                                if(count >= 5):
                                    winP2 = 1
                            else:
                                count = 0

                    # Verifica se tem cinco elementos 1 repetidos na diagonal principal
                    count = 0
                    # print(k)
                    # print(j)
                    if(10 - k >= 5):
                        for dp in range(10 - k):
                            if(j + dp < 10):
                                if(matriz[j + dp][k + dp] == 2):
                                    count += 1
                                    if(count >= 5):
                                        winP2 = 1
                                else:
                                    count = 0

                    # Verifica se tem cinco elementos 1 repetidos na diagonal inversa
                    count = 0
                    # if(k + 1 >= 5):
                    for di in range(k + 1):
                        if(j + di < 10):
                            if(matriz[j + di][k - di] == 2):
                                count += 1
                                if(count >= 5):
                                    winP2 = 1
                            else:
                                count = 0
        if(winP1 == 1 and winP2 == 0):
            print("1")
        elif(winP2 == 1 and winP1 == 0):
            print("2")
        else:
            print("Não há um vencedor")
    elif(option == 2):
        matriz = []
        winP1 = 0
        winP2 = 0
        for i in range(10):
            matriz.append([])
            for j in range(10):
                matriz[i].append(randint(0, 2))
        for j in range(10):
            for k in range(10):
                if(matriz[j][k] == 1):
                    count = 0
                    # Verifica se tem cinco elementos 1 repetidos na horizontal
                    if(10 - k >= 5):
                        for l in range(10 - k):
                            if(matriz[j][k + l] == 1):
                                count += 1
                                if(count >= 5):
                                    winP1 = 1
                            else:
                                count = 0
                    # Verifica se tem cinco elementos 1 repetidos na vertical
                    count = 0
                    if(10 - j >= 5):
                        for c in range(10 - j):
                            if(matriz[j + c][k] == 1):
                                count += 1
                                if(count >= 5):
                                    winP1 = 1
                            else:
                                count = 0

                    # Verifica se tem cinco elementos 1 repetidos na diagonal principal
                    count = 0
                    # print(k)
                    # print(j)
                    if(10 - k >= 5):
                        for dp in range(10 - k):
                            if(j + dp < 10):
                                if(matriz[j + dp][k + dp] == 1):
                                    count += 1
                                    if(count >= 5):
                                        winP1 = 1
                                else:
                                    count = 0

                    # Verifica se tem cinco elementos 1 repetidos na diagonal inversa
                    count = 0
                    # if(k + 1 >= 5):
                    for di in range(k + 1):
                        if(j + di < 10):
                            if(matriz[j + di][k - di] == 1):
                                count += 1
                                if(count >= 5):
                                    winP1 = 1
                            else:
                                count = 0

                if(matriz[j][k] == 2):
                    count = 0
                    # Verifica se tem cinco elementos 1 repetidos na horizontal
                    if(10 - k >= 5):
                        for l in range(10 - k):
                            if(matriz[j][k + l] == 2):
                                count += 1
                                if(count >= 5):
                                    winP2 = 1
                            else:
                                count = 0
                    # Verifica se tem cinco elementos 1 repetidos na vertical
                    count = 0
                    if(10 - j >= 5):
                        for c in range(10 - j):
                            if(matriz[j + c][k] == 2):
                                count += 1
                                if(count >= 5):
                                    winP2 = 1
                            else:
                                count = 0

                    # Verifica se tem cinco elementos 1 repetidos na diagonal principal
                    count = 0
                    # print(k)
                    # print(j)
                    if(10 - k >= 5):
                        for dp in range(10 - k):
                            if(j + dp < 10):
                                if(matriz[j + dp][k + dp] == 2):
                                    count += 1
                                    if(count >= 5):
                                        winP2 = 1
                                else:
                                    count = 0

                    # Verifica se tem cinco elementos 1 repetidos na diagonal inversa
                    count = 0
                    # if(k + 1 >= 5):
                    for di in range(k + 1):
                        if(j + di < 10):
                            if(matriz[j + di][k - di] == 2):
                                count += 1
                                if(count >= 5):
                                    winP2 = 1
                            else:
                                count = 0
        if(winP1 == 1 and winP2 == 0):
            print("1")
        elif(winP2 == 1 and winP1 == 0):
            print("2")
        else:
            print("Não há um vencedor")

    elif(option == 3):
        break
