# 5)	Faça um programa que peça um número inteiro e
# determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

count = 0
num = int(input("Digite um inteiro: "))

for i in range(1, num + 1):
    if(num % i == 0):
        count += 1

if(count == 2):
    print(f"" + str(num) + " eh primo")
else:
    print(f"" + str(num) + " nao eh primo")
