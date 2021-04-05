n = int(input())
i = 0
totalC = 0
totalR = 0
totalS = 0
total = 0
while(i < n):
    q, t = input().split()
    q = int(q)
    if(t.upper() == "C"):
        totalC += q
    elif(t.upper() == "R"):
        totalR += q
    else:
        totalS += q

    total = totalC + totalR + totalS
    i += 1
percC = totalC * 100 / total
percR = totalR * 100 / total
percS = totalS * 100 / total
print("Total: ", total)
print("Total de coelhos: ", totalC)
print("Total de ratos: ", totalR)
print("Total de sapos: ", totalS)
print("Percentual de coelhos: ", round(percC, 2), "%")
print("Percentual de ratos: ", round(percR, 2), "%")
print("Percentual de sapos: ", round(percS, 2), "%")
