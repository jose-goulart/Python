dic = {}
dicArray = []
x = int(input())
if(3 <= x <= 20):
    i = 0
    while(i < x):
        n, p1, p2, p3 = input().split()
        dic["nome"] = n
        dic["p1"] = p1
        dic["p2"] = p2
        dic["p3"] = p3
        dicArray.append(dic.copy())
        i +=1
    
    while True:
        count = 0
        n2, p = input().split()
        for j in range(len(dicArray)):
            if(n2 == dicArray[j]["nome"]):
                if(p == dicArray[j]["p1"] or p == dicArray[j]["p2"] or p == dicArray[j]["p3"]):
                    count += 1
        if(count >= 1):
            print("Uhul! Seu amigo secreto vai adorar o/")
        else:
            print("Tente Novamente!")
        