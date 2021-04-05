#Entrada dos dados via teclado
#Total de eleitores do município
totalVoters = int(input("Digite a quantidade total de eleitores do município: "))

if totalVoters != 0:
    #Entrada dos dados via teclado
    #Total de votos brancos
    blankVotes = int(input("Digite o número de votos brancos: "))
    #Total de votos nulos
    nullVotes = int(input("Digite o número de votos nulos: "))
    #Total de votos válidos
    validatedVotes = int(input("Digite a quantidade de votos válidos: "))
    
    #Faz a validação para ver se existe algum voto branco, nulo ou válido
    if blankVotes != 0:
        #Calcula percentual de votos brancos, nulos e válidos em relação ao total de eleitores
        blankPercentage = (blankVotes * 100) / totalVoters
        print(f"Porcentagem de votos brancos: {blankPercentage}%")
        #Caso nao tenha votos branco
    else:
        print("Não há nenhum voto branco!")
    if nullVotes != 0:
        nullPercentage = (nullVotes * 100) / totalVoters
        print(f"Porcentagem de votos nulos: {nullPercentage}%")
        #Caso nao tenha votos nulos
    else:
        print("Não há nenhum voto nulo!")
    if validatedVotes != 0:
        validatedPercentage = (validatedVotes * 100) / totalVoters
        print(f"Porcentagem de votos válidos: {validatedPercentage}%")
        #Caso nao tenha votos válidos
    else:
        print("Não há nenhum voto válido!")
        
    #Calcula total de votos brancos, nulos e válidos
    totalBlankNullValidated = blankVotes + nullVotes + validatedVotes
    
    if totalBlankNullValidated == totalVoters:
        print("O número total de votos é igual ao de eleitores!")
    elif totalBlankNullValidated > totalVoters:
        print("Houve fraude!")
    else:
        print("O número total de votos é diferente do de eleitores!")

#se nao existirem eleitores imprime
else:
    print("Não há nenhum voto para ser contabilizado!")




