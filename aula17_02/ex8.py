# 8)	Faça um programa que receba dois números inteiros e 
# gere os números inteiros que estão no intervalo compreendido por eles. 
# No final mostre a soma dos números (do intervalo).

numA, numB = [int(x) for x in(input("Digite dois numeros inteiros: ")).split()]

if(numA < numB):
    for i in range(numA + 1, numB):
        print(i)
elif(numA > numB):
    for i in range(numA - 1, numB, -1):
        print(i)