n = 0
count = 0
sum = 0
while(n != 123):
    n = int(input("Digite um número inteiro: "))
    if(n != 123):
        sum += n
    count += 1
print(f"Vc digitou {count} nmros. Soma dos numeros igual a: {sum}")
