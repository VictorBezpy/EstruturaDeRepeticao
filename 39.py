#39.py
"""
39. Faça um programa que leia dez conjuntos de dois valores, o primeiro 
representando o número do aluno e o segundo representando a sua altura em
centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do 
aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""
altura = []
alunos = []
k = 0

while k <= 9:
	aluno = int(input('Digite o número do aluno: '))
	alunos.append(aluno)
	alt = int(input('Digite a altura  do aluno em cm: '))
	altura.append(alt)
	k += 1
print('O aluno', alunos[altura.index(max(altura))], 
', é o mais alto com', max(altura), 'cm.')
print('O aluno', alunos[altura.index(min(altura))], 
', é o mais baixo com', min(altura), 'cm.')
