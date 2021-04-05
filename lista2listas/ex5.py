n = int(input())
c = []
if(1 <= n <= 50):
    i = 0
    while(i < n):
        c.append(int(input()))
        i += 1
    for i in range(len(c)):
        count = 0
        if(i == 0):
            if(c[1] == 1):
                count += 1
            if(c[i] == 1):
                count += 1
            print(count)
        elif(i == len(c) - 1):
            if(c[len(c) - 2] == 1):
                count += 1
            if(c[i] == 1):
                count += 1
            print(count)
        else:
            if(c[i - 1] == 1):
                count += 1
            if(c[i + 1] == 1):
                count += 1
            if(c[i] == 1):
                count += 1
            print(count)
else:
    print("A numero de linhas deve ser entre [1;50]")