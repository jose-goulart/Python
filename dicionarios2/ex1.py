import string
atoz = list(string.ascii_lowercase)

dic = {}
dicArray = []
total = []
sumArray = []
values = []

m, n = [int(x) for x in input("Digite dois nmros inteiros: ").split()]
i = 0
if(m <= 1000 and n <= 100):
    while(i < m):
        word, value = input("Palavra e valor: ").split()
        value = float(value)
        dic["word"] = word
        dic["value"] = value
        dicArray.append(dic.copy())
        total.append(dic.copy())
        # if(len(word) <= 16):
        #     if(0 <= value <= 1000000):
        #         print()                
        # else:
        #     print("Digite uma palavra de até 16 chars!")
        i += 1   
    i = 0

    
    
    # print(total)
    while(i < n):
        description = []
        description.append(input("Descrição 1 do cargo: "))
        nospace = description[0].replace(" ", "")
        while(nospace != "."):
            j = 0
            description.append(input("Descrição 2 do cargo: "))
            while(j < len(description)):
                nospace = description[j].replace(" ", "")
                j += 1
        else:
            l = 0
            while(l < len(total)):
                sum = 0
                j = 0
                while(j < len(description)):
                    countWord = description[j].count(total[l]["word"])
                    sum += countWord
                    total[l]["value"] = float(sum)
                    j +=1
                l += 1  
                # print(total)
                # print(sum)
            i += 1
        t=0
        # print(total[0]["value"] * dicArray[t]["value"])
        while(t < len(total)):
            total[t]["value"] = (dicArray[t]["value"] * total[t]["value"])
            sumArray.append(total[t]["value"])
            t+=1

b = 0
e = n
for z in range(n):
    sum = 0
    for x in range(b,e):
        sum += sumArray[x]
        while(e < len(sumArray)):
            e += n
            b += n
    values.append(sum)
for y in values:
    print(y)   
        # print(sum)
        # VALIDAÇÕES
        # else:
        #     count = 0
        #     for j in range(len(nospace)):
        #         for k in atoz:
        #             if(nospace[j] == k):
        #                 count += 1
        #     if(len(nospace) == count):
        #         i += 1
        #     else:
        #         print("Invalido")