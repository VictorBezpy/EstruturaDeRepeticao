#27.py
"""
27. Faça um programa que calcule o número médio de alunos por turma. Para isto,
peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas 
não podem ter mais de 40 alunos.
"""
qt = int(input('quantidade de turmas: '))
notas = []
i = 1
while i <= qt:
	n = int(input('alunos na turma: '))
	if n <= 40:
		notas.append(n)
		i += 1
	else:
		print('máximo 40 alunos por turma.')
soma = 0
i = 0
while i <= qt - 1:#vagões [0 1 2 3 4] por isso - 1
	soma += notas[i]
	i += 1

print('média de alunos por turma: %.2f' %(soma/qt))