def sumArray(array):
    sum = 0
    for i in array:
        sum += i
    return sum


m = [[], [], []]
evenPos = []
sumThirdC = []
highest = 0
for i in range(3):
    for j in range(3):
        m[i].append(int(input()))
for k in range(3):
    for l in range(3):
        if(l == 2):
            print(f"[{m[k][l]}]")
        else:
            print(f"[{m[k][l]}]", end=" ")
        if(m[k][l] % 2 == 0):
            evenPos.append(m[k][l])
        if(l == 0):
            highest = m[1][0]
        elif(m[1][l] > highest):
            highest = m[1][l]

    sumThirdC.append(m[k][2])


print(sumArray(evenPos))
print(sumArray(sumThirdC))
print(highest)
