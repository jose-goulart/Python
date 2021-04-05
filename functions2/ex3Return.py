def evenorodd(x):
    if(x % 2 == 0):
        result = "Par"
        return result
    else:
        result = "Impar"
        return result
i = 0
even = 0
odds = 0
while(i <= 9):
    x = int(input())
    result = evenorodd(x)
    print(result)
    if(result == "Par"):
        even += 1
    else:
        odds += 1
    i += 1
print(f"{even} Pares e {odds} Impares")