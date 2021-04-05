name = input("Digite o nome do vendedor: ")
salary = float(input("Digite o salario fixo do vendedor: "))
totalSold = float(input("Digite o total de vendas: "))

total = round(salary + (totalSold * 0.15), 2)
print(f"TOTAL = R$ {total}")