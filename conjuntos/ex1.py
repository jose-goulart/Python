soccer = {"João", "Maicon"}
swimming = {"Gabriela", "Alysson"}
voley = {"Pedro", "Thiago", "Patricia"}
basket = {"Gabriel", "Juliano"}

print("Futebol:", soccer)
print("Natação:", swimming)
print("Vôlei:", voley)
print("Basquete:", basket)

name = input("Digite seu nome: ")
while(True):
    mod = int(input("Qual das Modalidades vc quer se matricular?\n1 - Futebol\n2 - Natação\n3 - Vôlei\n4 - Basquete"))
    if(mod == 1):
        soccer.add(name)
    elif(mod == 2):
        swimming.add(name)
    elif(mod == 1):
        voley.add(name)
    else:
        basket.add(name)
    answer = input("Deseja se matricular em mais alguma?\nS - Sim\nN - Não")
    if(answer.upper() == "N"):
        break

print("Futebol:", soccer)
print("Natação:", swimming)
print("Vôlei:", voley)
print("Basquete:", basket)