#Lê a idade de uma pessoa em anos, meses e dias
years, months, days = [int(x) for x in input("Digite a sua idade: ").split()]

#Valida se meses e anos é diferente de zero
if years != 0 and months != 0:
    #Calcula quantos dias tem na quantidade
    #de anos e meses que foi inserido
    yearsDays = years * 365
    monthsDays = months * 30
    #Soma os dias, meses e anos
    ageDays = days + monthsDays + yearsDays
    
elif years != 0:
    #Calcula quantos dias tem na quantidade
    #de anos
    yearsDays = years * 365
    #Soma os dias e anos
    ageDays = days + yearsDays

elif months != 0:
    #Calcula quantos dias tem na quantidade
    #de meses
    monthsDays = months * 30
    #Soma os dias e meses
    ageDays = days + monthsDays
else:
    #Seta total igual a dias caso a
    #quantidade de meses e anos seja igual a zero
    ageDays = days

#Imprimir a idade expressa em dias
if ageDays > 1:
    print(f"{ageDays} Dias de Idade!")
else:
    print(f"{ageDays} Dia de Idade!")