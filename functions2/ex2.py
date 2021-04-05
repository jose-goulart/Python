def fusoh(a,b,c):
    arrived = a + b + (c)
    while(arrived > 24):
        arrived -= 24
    while(arrived <= 0):
        arrived += 24
    print(arrived)
a,b,c = [int(x) for x in input().split()]
fusoh(a,b,c)