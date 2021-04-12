person = {}
dicArray = []
women = []
aboveAvg = []

for i in range(4):
    person['name'] = input("Nome: ")
    person['gen'] = input("Sexo: ")
    person['age'] = int(input("Idade: "))
    dicArray.append(person.copy())
sum = 0
for i in range(4):
    sum += dicArray[i]['age']
    if(dicArray[i]['gen'].upper() == "F"):
        women.append(dicArray[i]['name'])
avg = sum / len(dicArray)

for i in range(4):
    if(dicArray[i]['age'] > avg):
        aboveAvg.append(dicArray[i]['name'])

print(f"Número de pessoas cadastradas: {len(dicArray)}")
print(f"Média de idade do grupo: {avg}")
print(f"Todas as mulheres: {women}")
print(f"Pessoas acima da média: {aboveAvg}")
