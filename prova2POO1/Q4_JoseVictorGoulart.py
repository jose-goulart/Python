# Nome: José Victor Goulart dos Santos
# Matrícula: 20200412
i = 0
dict = {}
arrayDict = []
n, m = [int(x) for x in input().split()]
while(i < m):
    a, b, c = [int(x) for x in input().split()]
    if(a >= n or b > n):
        print(f"Existem apenas {n} cidades!")
    else:
        dict['a'] = a
        dict['b'] = b
        dict['c'] = c
        arrayDict.append(dict.copy())
        i += 1
print(arrayDict)