from random import randint

numRand = randint(0,10)
attempts = 1
num = int(input("Advinhe o valor entre 0 e 10: "))
while(num != numRand):
    num = int(input("Tente novamente: "))
    attempts+=1

print(f"Correto. Você tentou {attempts} vezes para acertar o número {numRand}")