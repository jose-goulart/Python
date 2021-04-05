# 7)	Faça um programa que peça para n pessoas a sua idade, 
# ao final o programa deverá verificar se a média de idade da turma varia 
# entre 0 e 25, 26 e 60 e maior que 60; e então, 
# dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
sumOfAge = 0
qtdPeople = int(input("Quantas pessoas há na turma? "))

for i in range(0, qtdPeople):
    age = int(input("Digite sua idade: "))
    sumOfAge += age;
avg = sumOfAge / qtdPeople
avg = float(avg)
if(0 <= avg <= 25):
    print(f"Turma Jovem. Média: " + str(avg))
elif(26 <= avg <= 60):
    print(f"Turma Adulta. Médi a: " + str(avg))
else:
    print(f"Turma Idosa. Média: " + str(avg))


