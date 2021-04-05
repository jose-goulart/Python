# 5) Implemente um programa que calcule a média de idade de um grupo de
# amigos.
# - Usuário decide o momento de parada de inserir as idades, por exemplo, a cada
# inserção de idade perguntar se deseja continuar cadastrando.

ask = "S"
tot = 0
count = 0
while(ask.upper() == "S"):
    age = int(input("Digite a idade: "))
    tot += age
    ask = input("Deseja continuar cadastrando? ")
    count += 1
tot = tot / count
print(f"Media: {tot}")