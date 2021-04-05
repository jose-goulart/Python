# 4) Elabore um programa que, para um número inteiro positivo N, 
# determine se esse número é par ou não.

num = int(input("Digite um numero inteiro: "))

if(num % 2 == 0):
    print(f"O numero {num} eh par")
else:
    print(f"O numero {num} eh impar")