# 9) Considerando uma turma de 3 alunos, faça um algoritmo que 
# leia os valores das notas e calcule a média da turma.

student1, student2, student3 = [float (x) for x in input("Digite as notas dos alunos 1, 2 e 3: ").split()]

classAvg = (student1 + student2 + student3) / 3

print(f"A media da turma foi igual a: {classAvg}")