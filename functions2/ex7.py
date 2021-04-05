def elevator(n,c):
    i = 1
    now = 0
    while(i <= n):
        s, e = [int(x) for x in input().split()]
        if(now > c):
            out = "S"
        else:
            out = "N"
        now -= s
        now += e
        i += 1
    print(out)

n, c = [int(x) for x in input().split()]
elevator(n,c)