
result = 0
arrayScores = []
while(True):
    score = 0
    n, m = [int(x) for x in input("").split()]
    if(n >= 3 and m <= 100):
        array = []
        stop = 0

        # COLOCA AS LINHAS DENTRO DE UM ARRAY FORMANDO UMA MATRIZ
        for i in range(n):
            # N LINHAS
            ij = [int(x) for x in input("").split()]
            array.append(ij[:])
        # PRIMEIRA CARACTERÍSTICA
        count = 0
        for k in range(len(array)):
            for l in range(len(array[k])):
                if(array[k][l] == 1):
                    count += 1
        if(count != m):
            score += 1
        # FIM PRIMEIRA CARACTERÍSTICA

        # SEGUNDA CARACTERÍSTICA
        count = 0
        for k in range(m):
            for v in [x[k] for x in array]:
                if(v == 1):
                    count += 1
        if(count >= m):
            score += 1
        # FIM SEGUNDA CARACTERÍSTICA

        # TERCEIRA CARACTERÍSTICA
        count = 0
        for k in range(m):
            for v in [x[k] for x in array]:
                if(v == 0):
                    count += 1
        if(count >= m):
            score += 1
        # FIM TERCEIRA CARACTERÍSTICA

        # QUARTA CARACTERÍSTICA
        count = 0
        for k in range(len(array)):
            s = 0
            for l in array[k]:
                if(l == 1):
                    s += 1
            if(s >= 1):
                count += 1
        if(count >= n):
            score += 1
        # FIM QUARTA CARACTERÍSTICA

    else:
        if(n == 0 and m == 0):
            break
        else:
            print("O primeiro deve ser >= 3 o segundo deve ser <= 100")
            n, m = [int(x) for x in input("").split()]
    arrayScores.append(score)
for i in arrayScores:
    print(i, end="\n")