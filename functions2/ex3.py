def passZ(x,z):
    z = 0
    count = 2
    while(z <= x):
        z = int(input())
    else:
        while(x <= z):
            x += x + 1
            count += 1
        print(count)

x = int(input())
z = int(input())
passZ(x,z)