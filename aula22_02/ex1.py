even = 0
odd = 0
positive = 0
negative = 0
for i in range(1,6):
    n = int(input(f"Digite o {i}º inteiro: "))
    if(n % 2 == 0):
        even +=1
    else:
        odd+=1
    if(n > 0):
        positive +=1
    elif(n < 0):
        negative+=1
print(f"Pares: {even}\nImpares: {odd}\nPositivos: {positive}\nNegativos: {negative}")