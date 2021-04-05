while(True):
    n,m = input().split()
    n = int(n)
    total = 0    
    for i in range(0, n):
        mIndex = m[i]
        total += int(mIndex)
    print(total, end=' ')
    if(total % 3 == 0):
        print("Sim")
    else:
        print("Nao")
    ask = input("Continuar? N - nao S - sim")
    if(ask.upper() == "N"):
        break
