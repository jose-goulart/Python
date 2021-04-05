# 6)	Altere o programa de cálculo dos números primos (exercício 5), 
# informando, caso o número não seja primo, 
# por qual(is) número(s) ele é divisível.

count = 0
divisors = []
num = int(input("Digite um inteiro: "))

for i in range(1, num + 1):
    if(num % i == 0):
        count += 1
        divisors.append(i)
if(count != 2):
    print(f"" + str(num) + " Não é primo; É divisível por: " + str(divisors)[1:-1])

