# 1) Faça o implementação do jogo pedra-papel-tesoura. O jogo deve imprimir
# vitória, empate ou derrota conforme a opção que os jogadores escolherem.
# Obs.: pedra ganha de tesoura, que ganha de papel, que ganha de pedra.
# Perguntar ao usuário se ele deseja continuar jogando.
from random import randint

print("Pedra -> 1\nPapel -> 2\nTesoura -> 3")
ask = "S"
while(ask.upper() == "S"):
    cpu = randint(1, 3)
    p1 = int(input("Pedra, Papel ou Tesoura? "))
    if(p1 == 1):
        elem1 = "Pedra"
    elif(p1 == 2):
        elem1 = "Papel"
    else:
        elem1 = "Tesoura"
    if(cpu == 1):
        elem2 = "Pedra"
    elif(cpu == 2):
        elem2 = "Papel"
    else:
        elem2 = "Tesoura"
    print(f"Você jogou {elem1} e o computador jogou {elem2}: ", end="")
    if(cpu == 1):
        if(p1 == 1):
            print("Empate")
        if(p1 == 2):
            print("Vitória")
        if(p1 == 3):
            print("Derrota")
    elif(cpu == 2):
        if(p1 == 1):
            print("Derrota")
        if(p1 == 2):
            print("Empate")
        if(p1 == 3):
            print("Vitória")
    else:
        if(p1 == 1):
            print("Vitória")
        if(p1 == 2):
            print("Derrota")
        if(p1 == 3):
            print("Empate")
    ask = input("Deseja continuar? ")
