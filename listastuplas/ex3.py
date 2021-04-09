tuple = (2, 7, 6, 9, 10, 5, 3, 2, 1, 7)
highest = 0
lowest = 0

for i in range(10):
    if(highest == 0):
        highest = tuple[0]
        positionHighest = 0
    elif(tuple[i] >= highest):
        highest = tuple[i]
        positionHighest = i

    if(lowest == 0):
        lowest = tuple[0]
        positionLowest = 0
    elif(tuple[i] <= lowest):
        lowest = tuple[i]
        positionLowest = i

print("Posição Maior valor:", positionHighest)
print("Posição Menor valor:", positionLowest)