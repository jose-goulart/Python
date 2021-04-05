n = int(input("Digite um inteiro: "))
square = 0
if(n >= 1):
    for i in range(0, n + 1):
        square += i * i
    print(square)
