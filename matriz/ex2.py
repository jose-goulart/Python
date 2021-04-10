from inputFunction import getInput
from random import uniform

m = []

for i in range(12):
    m.append([])

t = input("Operação S ou M: ")

array = getInput("", float, 144, 0, 11)

# ESSE FOR ABAIXO INSERE 144 VALORES
# FLOAT ENTRE 0 E 11 NO ARRAY PARA TESTAR
# array = []
# for p in range(144):
#     number = uniform(0,11)
#     array.append(number)

b = 0
e = 12
for j in range(12):
    for k in range(b, e):
        m[j].append(array[k])
    b += 12
    e += 12

b = 0
s = 0
i = 0

for j in range(1, 12):
    if(j == 1):
        rangeK = 1
    else:
        rangeK = j

    for k in range(rangeK):
        s += m[j][k]
        i +=1


if(t.upper() == "S"):
    print(f"Soma dos elementos abaixo da diagonal principal: {s}")

elif(t.upper() == "M"):
    avg = round(s / i, 1)
    print(f"Média dos elementos abaixo da diagonal principal: {avg}")
