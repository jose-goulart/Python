n = int(input())
i = 0

while(i < n):
    cmd = input()
    if(cmd[0] == cmd[2]):
        mult = int(cmd[0]) * int(cmd[2])
        print(mult)
    elif(cmd[1] == cmd[1].lower()):
        sum = int(cmd[0]) + int(cmd[2])
        print(sum)
    elif(cmd[1] == cmd[1].upper()):
        sub = int(cmd[2]) - int(cmd[0])
        print(sub)
    i+=1