# 4)	Faça um programa que peça ao usuário para digitar 10 números inteiros, 
# ao final seu programa deve mostrar a quantidade de números 
# pares e a quantidade de números impares.
countPair = 0
countOdd = 0
for i in range(0, 10):
    numberInt = int(input("Digite 1 inteiro: "))
    if(numberInt % 2 == 0):
        countPair += 1
    else:
        countOdd += 1
print(f"Qtd pares: " + str(countPair) + " Qtd impares: " + str(countOdd))
