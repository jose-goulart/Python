from Funcionario import Employee
i = 0
while(i < 3):
    name = input("Digite o nome do funcionário: ")
    currentSalary = float(input("Digite o salário atual do funcionário: "))

    if(currentSalary < 1500):
        print("Digite um valor igual ou maior a 1500")
    else:
        f = Employee(name, currentSalary)
        f.updateSalary()
        i += 1
