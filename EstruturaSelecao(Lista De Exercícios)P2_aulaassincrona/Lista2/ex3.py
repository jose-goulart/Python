# 3) Elabore um programa que, dada a idade de uma pessoa,
# informe se esta é criança, adolescente ou adulto.
# Considere as seguintes faixas etárias:
# Idade até 12 anos:				Criança
# Idade maior que 12 e menor que 18 anos:	Adolescente
# Idade maior ou igual a 18 anos:		Adulto

age = int(input("Digite sua idade: "))

if(age <= 12):
    print("Crianca")
elif(12 < age < 18):
    print("Adolescente")
else:
    print("Adulto")
