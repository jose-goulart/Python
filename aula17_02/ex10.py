# 10) Considerar uma turma da Disciplina de Cálculo I, com 5 alunos,
# fazer um programa que:
# 10.1)	Calcule a média das notas;
# 10.2)	Indique o nome do aluno com a média mais alta
# 10.3)	Informe seu conceito (Aprovado, Em Recuperação, Reprovado).
# Considerando que essas regras funcionam da mesma forma que na UFSC: se a
# média for 5.75 ou maior, o aluno está aprovado, se a nota for maior ou
# igual a 2.75, ele tem o direito de fazer a prova de recuperação e se o ,
# aluno obtiver uma média menor que 2.75 ele foi reprovado.
sumOfScore = 0
highestScore = 0
bestStudent = ""
concept = ""
for i in range(0, 5):
    score = float(input("Digite sua nota: "))
    name = input("Digite seu nome: ")
    sumOfScore += score
    avg = sumOfScore / 5

    if(score >= highestScore):
        highestScore = score
        bestStudent = name
        if(score >= 5.75):
            concept = "Aprovado"
        elif(score >= 2.75):
            concept = "Recuperação"
        else:
            concept = "Reprovado"

print(f"Média das notas de todos alunos: {avg}")
print(f"Aluno com maior nota: {bestStudent}. Nota: {highestScore}")
print(f"Conceito do aluno: {concept}")
