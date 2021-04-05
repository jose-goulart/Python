n = int(input("Qtd de valores para digitar: "))

for i in range(1, n + 1):
    n = int(input("Digite um um inteiro: "))
    if(n % 2 != 0):
        print("ODD", end=" ")
    elif(n == 0):
        print("NULL")
    else:
        print("EVEN", end=" ")
    if(n < 0):
        print("NEGATIVE")
    elif(n > 0):
        print("POSITIVE")