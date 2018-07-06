#21-primo.py
"""
21. Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele mesmo e 
por 1.
"""
n = int(input('Digite um número: '))
total = 0
for c in range(1, n + 1):
	if n % c == 0:
		total += 1
if total == 2:
	print(n, 'é um número primo.')
else:
	print(n, 'não é um número primo.')