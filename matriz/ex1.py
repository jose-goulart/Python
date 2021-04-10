# from inputFunction import getInput
# from random import uniform

m = []

for i in range(12):
    m.append([])

l = int(input())
t = input("Operação S ou M: ")

# array = getInput("", float, 144, 0, 11)

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

s = 0
for i in m[l]:
    s += i
if(t.upper() == "S"):
    print(f"Soma dos elementos da linha {l}: {s}")

elif(t.upper() == "M"):
    avg = round(s / (len(m[l])),1)
    print(f"Média dos elementos da linha {l}: {avg}")
