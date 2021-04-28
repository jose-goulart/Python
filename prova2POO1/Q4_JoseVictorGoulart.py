# Nome: José Victor Goulart dos Santos
# Matrícula: 20200412
i = 0
dict = {}
arrayDict = []
while True:
    n, m = [int(x) for x in input().split()]
    if(2 <= n <= 10 and 1<= m <= 10):
        break
    else:
        print("N deve estar entre 2 e 10 (ambos inclusos) e m entre 1 e 100 (ambos inclusos)")

while(i < m):
    a, b, c = [int(x) for x in input().split()]
    if(1 <= a <= n and 1 <= b <= n and a != b and 1 <= c <= 100):
        if(a >= n or b > n):
            print(f"Existem apenas {n} cidades!")
        else:
            dict['a'] = a
            dict['b'] = b
            dict['c'] = c
            arrayDict.append(dict.copy())
            i += 1
    else:
        print("1 <= A,B <= N e A != B")
        print("1 <= C <= 100")
i = 0
while(i < len(arrayDict)):
    routs = []
    s = 0
    while(s < )
    # if(i < len(arrayDict) - 1):
        # print(arrayDict[i + 1]["a"])
        # print(arrayDict[i]["b"])
        # if(arrayDict[i + 1]["a"] == arrayDict[i]["b"]):
        #     routs.append(arrayDict[i])
        #     print(arrayDict[i])
        # print(arrayDict[i]["c"])
    i += 1
print(routs)
print(arrayDict)