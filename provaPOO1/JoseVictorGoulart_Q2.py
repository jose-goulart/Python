# Nome: José Victor Goulart dos Santos
# Matrícula: 20200412

ask = "S"
avg = 0
count = 0
mupper2 = 0
lowestSalary = 0
genderLowestSalary = 0
ageLowestSalary = 0
salary = 0
while(ask.upper() == "S"):
    age, gender, salary = input().split()
    age = int(age)
    salary = float(salary)
    avg += age
    # condicional para contar mulheres que ganham mais de 2000
    if(gender.upper() == "F" and salary > 2000):
        mupper2 += 1
    count += 1
    # condicional para setar o menor salario que será digitado,
    # e assim ser definida a idade e sexo
    if(lowestSalary == 0):
        lowestSalary = salary
        ageLowestSalary = age
        genderLowestSalary = gender
    elif(salary <= lowestSalary):
        lowestSalary = salary
        ageLowestSalary = age
        genderLowestSalary = gender

    ask = input("Deseja continuar ?")
avg = avg / count
print(f"Média de idade: {avg}\nMulheres com salário maior que R$2.000,00: {mupper2}\nMenor salário, Sexo: {genderLowestSalary} Idade: {ageLowestSalary}")
