#24.py
"""
24. Faça um programa que calcule o mostre a média aritmética de N notas.
"""
q = int(input('quantidade: '))
notas = []
i = 1
while i <= q:
	n = float(input('nota: '))
	notas.append(n)
	i += 1
soma = 0
i = 0
while i <= q - 1:#vagões [0 1 2 3 4] por isso - 1
	soma += notas[i]
	i += 1

print('média: %.2f' %(soma/q))