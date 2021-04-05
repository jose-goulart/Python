def cartesian(x, y):
    if(x > 0):
        if(y > 0):
            print("primeiro")
        elif(y < 0):
            print("quarto")
    if(x < 0):
        if(y > 0):
            print("segundo")
        elif(y < 0):
            print("terceiro")

while(True):
    x, y = [int(x) for x in input().split(" ")]
    cartesian(x, y)
    if(x == 0 or y == 0):
        break
