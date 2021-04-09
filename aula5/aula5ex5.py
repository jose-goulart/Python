qtd = float(input("Quantos salários vc quer calcular? "))
count = 1
porcentage = 0.11

while(count <= qtd):
    salary = float(input("Digite o salario: "))
    discount = salary * porcentage
    if(discount <= 318.20):
        salary -= discount
    else:
        salary -= 318.20
    print(f"Salario {count}: = R$ {salary}")
    count +=1