# 4) Faça um programa que solicite ao usuário para digitar 3 número inteiros, seu
# programa deverá ordená-los. O programa somente será encerrado quando o 
# usuário desejar. (após apresentar os números ordenados, pergunte se o usuário
# quer digitar novos números).
n1 = 0
n2 = 0
n3 = 0
i = 0
ask = "S"
while(ask.upper() == "S"):
    while(i <= 2):
        n = int(input("Digite 1 inteiro: "))
        if(i == 0):
            n1 = n
        if(i == 1):
            n2 = n
        else:
            n3 = n
        i += 1
    if(n3 > n2 > n1):
        print(f"Nmros ordenados: {n1}-{n2}-{n3}")
    elif(n2 > n3 > n1):
        print(f"Nmros ordenados: {n1}-{n3}-{n2}")
    elif(n3 > n1 > n2):
        print(f"Nmros ordenados: {n2}-{n1}-{n3}")
    elif(n1 > n3 > n2):
        print(f"Nmros ordenados: {n2}-{n3}-{n1}")
    elif(n2 > n1 > n3):
        print(f"Nmros ordenados: {n3}-{n1}-{n2}")
    else:
        print(f"Nmros ordenados: {n3}-{n2}-{n1}")
    ask = input("Deseja repetir? S - sim N - nao")
    i =0