n = int(input("Digite um um inteiro: "))

for i in range(1, n + 1):
    if(i % 2 == 0):
        square = i * i
        print(f"{i}^2 = {square}")