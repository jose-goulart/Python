# 3)	Uma universidade particular oferece um desconto de 30% na
# mensalidade do aluno com melhor nota (média geral). Implemente um programa que
# após receber as informações do aluno (nome, nota/média geral, valor mensalidade)
# verifique quem é o aluno com melhor nota e calcule o desconto de sua mensalidade.
# Ao final de sua execução, o programa deve mostrar:
# - o nome do aluno com melhor nota,
# - o valor da mensalidade (sem desconto) e
# -  o valor da mensalidade com o desconto e 30%;
# Considerar 5 alunos (as informações devem ser lidas do teclado).
highestScore = 0
for i in range(0, 5):
    name, avg, valueMonthly = input(
        "Digite o nome, a nota e o valor da mensalidade: ").split()
    avg = float(avg)
    valueMonthly = float(valueMonthly)
    discount = 0.3 * valueMonthly
    if(i == 0):
        highestScore = avg
    if(highestScore <= avg):
        highestScore = avg
        valueMonthlyOff = valueMonthly - discount
print(f"Aluno com a maior nota: " + name)
print(f"Mensalidade: " + str(valueMonthly))
print(f"Mensalidade com desconto: " + name)
