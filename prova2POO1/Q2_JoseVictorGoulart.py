# Nome: José Victor Goulart dos Santos
# Matrícula: 20200412
def dist(x, y):
    avg = (abs(x) + abs(y)) / 2
    return avg
i = 0
dict = {}
arrayDict = []
n = int(input("Digite a quantidade de flechas lançadas: "))
while(i < n):
    x, y = [int(x) for x in input().split()]
    dict['x'] = x
    dict['y'] = y
    arrayDict.append(dict.copy())
    i += 1
i = 0
sum = 0
temp = 0
while(i < len(arrayDict)):
    previous = dist(arrayDict[i]["x"], arrayDict[i]["y"])
    if(i < len(arrayDict) - 1):
        next = dist(arrayDict[i + 1]["x"], arrayDict[i + 1]["y"])
    if(previous <= next):
        sum = sum + temp
        temp += 1
    i += 1
print(sum)