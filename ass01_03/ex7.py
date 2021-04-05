n = int(input("Digite um inteiro: "))
i = 0
while(i <= n):
    if(i % 2 == 0 and i != 0):
        square = i * i
        print(f"{i}² = {square}")
    i += 1