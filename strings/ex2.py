n = int(input())
i = 0
c = 0
e = 0
last = 0
while(i < n):
    sd,sn = input().split()
    if(sd.lower() == "chuva" and sn.lower() == "chuva"):
        c += 1
    elif(sd.lower() == "sol" and sn.lower() == "chuva"):
        last = 1
        e += 1
    if(last == 1):
        if(sd.lower() == "chuva" and sn.lower() == "sol"):
            last = 0
    i += 1
print(c,e)