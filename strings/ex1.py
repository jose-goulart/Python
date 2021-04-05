position = 1
while(True):
    n = int(input())
    cmd = input()
    dChars = cmd.count("D")
    eChars = cmd.count("E")
    
    position += dChars
    position -= eChars
    if(position % 4 == 1 or position % 4 == -3):
        position = "N"
    elif(position % 4 == 2 or position % 4 == -2):
        position = "L"
    elif(position % 4 == 3 or position % 4 == -1):
        position = "S"
    else:
        position = "O"

    print(position)
    position = 1
    if(n == 0):
        break
