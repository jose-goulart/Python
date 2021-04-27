# Nome: José Victor Goulart dos Santos
# Matrícula: 20200412
import time

arrayD = []
employeeD = {}

while True:
    print("\n1 - Cadastrar funcionários")
    print("2 - Calcular idade em que o funcionário irá se aposentar")
    print("3 - Alterar dados do cadastro")
    print("4 - Consultar dados")
    print("5 - Sair do programa")
    option = input("Digite uma oção do menu: ")
    if(option == "1"):
        ask = "S"
        while(ask.upper() != "N"):
            print("Cadastrando funcionários\n")
            employeeD["name"] = input("Nome do funcionário(a): ")
            employeeD["age"] = int(input("Ano de nascimento (inteiro): "))
            employeeD["occupation"] = input("Cargo: ")
            employeeD["contYear"] = int(input("Ano da contratação (inteiro): "))
            employeeD["workerId"] = input("Número da carteira de trabalho: ")
            arrayD.append(employeeD.copy())
            ask = input("Deseja continuar? S - Sim N - Não\n")  
        time.sleep(2)
    elif(option == "2"):
        if(len(arrayD) > 0):
            i = 0
            retire = 0
            search = input("Digite o número da carteira de trabalho do funcionário: ")
            while(i < len(arrayD)):            
                if(search == arrayD[i]["workerId"]):
                    age = 2021 - arrayD[i]["age"]
                    contribution = 2021 - arrayD[i]["contYear"]
                    while(age < 61 or contribution < 35):
                        age += 1
                        contribution += 1
                    else:
                        print(f"O funcionário irá se aposentar com {age} anos")
                i += 1
            time.sleep(5)
        else:
            print("Ainda não existem funcionarios cadastrados!")
            time.sleep(2)
    elif(option == "3"):
        if(len(arrayD) > 0):
            i = 0
            search = input("Digite o nome do funcionário: ")
            while(i < len(arrayD)):            
                if(search.upper() == arrayD[i]["name"].upper()):
                    print("Alterando...")
                    arrayD[i]["name"] = input("Nome do funcionário(a): ")
                    arrayD[i]["occupation"] = input("Cargo: ")
                    arrayD[i]["workerId"] = input("Número da carteira de trabalho: ")
                i += 1
            time.sleep(2)
        else:
            print("Ainda não existem funcionarios cadastrados!")
            time.sleep(2)
    elif(option == "4"):
        if(len(arrayD) > 0):
            i = 0
            search = input("Digite o nome do funcionário: ")
            while(i < len(arrayD)):            
                if(search.upper() == arrayD[i]["name"].upper()):
                    print(f"Imprimindo dados do funcionário(a) {arrayD[i]['name']}...")
                    print(f"Nome do funcionário(a): {arrayD[i]['name']}")
                    print(f"Ano de nascimento: {arrayD[i]['age']}")
                    print(f"Cargo: {arrayD[i]['occupation']}")
                    print(f"Ano de contratação: {arrayD[i]['contYear']}")
                    print(f"Número da carteira de trabalho: {arrayD[i]['workerId']}")
                i += 1
                time.sleep(5)
        else:
            print("Ainda não existem funcionarios cadastrados!")
            time.sleep(2)
    if(option == "5"):
        break