def prime(x,y):
    i = 0
    primeN = 0
    for i in range(x, y + 1):
        count = 0
        for j in range(1, i + 1):
            if(i % j == 0):
                count += 1
        if(count == 2):
            primeN += 1
        i += 1
    return primeN

x,y = [int(x) for x in input().split()]
result = prime(x,y)
print(result)