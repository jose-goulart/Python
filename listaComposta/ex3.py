from random import randint
numbers = []
games = int(input("Quantos jogos serao sorteados? "))

for i in range(0, games):
    fraction = []
    for j in range(6):
        fraction.append(randint(1, 60))
    numbers.append(fraction)
    print(f"Jogo {i + 1}: {numbers[i]}")