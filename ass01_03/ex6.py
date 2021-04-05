# 6) Implementar um programa que calcule o aumento de salário dos funcionários
# de uma empresa. O aumento está condicionado ao atual salário de cada
# funcionário.
# Regras:
# - para 1.500,00 <= salarioAtual < 1.750,00: aumento igual a 12%;
# - para 1.750,00 <= salarioAtual < 2.000,00: aumento igual a 10%;
# - para 2.000,00 <= salarioAtual < 3.000,00: aumento igual a 7%;
# - para acima de 3.000,00: aumento igual a 5%.
# Calcular o aumento de no mínimo 3 funcionários;
# A cada cálculo efetuado mostrar um relatório com as seguintes informações:
# nome do funcionário, salário atual e salário com reajuste. 
i = 0
while(i <= 2):
    name = input("Digite o Nome: ")
    salary = float(input("Digite o salario: "))
    i += 1
    if(1500 <=salary < 1750):
        increase = salary * 0.12
        newsalary = salary + increase
    elif(1750 <=salary < 2000):
        increase = salary * 0.10
        newsalary = salary + increase
    elif(2000 <=salary < 3000):
        increase = salary * 0.07
        newsalary = salary + increase
    else:
        increase = salary * 0.05
        newsalary = salary + increase
    print(f"Nome do funcionario: {name}, salario atual: {salary}, Salario com reajuste: {newsalary}")