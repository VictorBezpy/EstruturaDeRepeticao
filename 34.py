#34.py
"""
34. Os números primos possuem várias aplicações dentro da Computação, por
exemplo na Criptografia. Um número primo é aquele que é divisível apenas por
um e por ele mesmo. Faça um programa que peça um número inteiro e determine
se ele é ou não um número primo.
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