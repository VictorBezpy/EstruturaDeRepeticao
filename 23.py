#23.py
"""
23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número
 inteiro fornecido pelo usuário. O programa deverá mostrar também o número de 
 divisões que ele executou para encontrar os números primos. 
"""
n = int(input('Digite um número: '))
total = 0
for c in range(1, n + 1):
	if n % c == 0:
		print('\033[33m', end='')
		total += 1
	else:
		print('\033[31m', end='')
	print('{} '.format(c), end='')
if total == 2:
	print('\n', n, 'é um número primo.')
else:
	print('\n', n, 'não é um número primo.')