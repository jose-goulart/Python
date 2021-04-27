from Clientes import Vip

dict = {}
dogs = []

i = 0
n = int(input("Quantos clientes vc deseja cadastrar? "))

while (i < n):
    breed = input("Raça: ")
    furColor = input("Cor do pelo: ")
    weight = float(input("Peso: "))
    age = int(input("Idade: "))
    dogName = input("Nome do animal: ")
    ownerName = input("Nome do dono: ")
    foodRestric = input("Restrição alimentar: S - Sim N - Não")
    bathFrequency = int(input("Periodicidade do banho: "))
    benefits = input("Vantagens: ")

    c = Vip(breed, furColor, weight, age, dogName,
            ownerName, foodRestric, bathFrequency, benefits)
    c.printInfo()
    print(c.foodRestriction(foodRestric))

    dict['breed'] = breed
    dict['furColor'] = furColor
    dict['weight'] = weight
    dict['age'] = age
    dict['dogName'] = dogName
    dict['ownerName'] = ownerName
    dict['foodRestric'] = foodRestric
    dict['bathFrequency'] = bathFrequency
    dict['benefits'] = benefits
    
    dogs.append(dict.copy())
    i += 1
print(c.oldestDog(dogs, n))