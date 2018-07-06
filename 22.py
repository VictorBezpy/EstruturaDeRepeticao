#22-primodiv.py
"""
22. Altere o programa de cálculo dos números primos, informando, caso o número 
não seja primo, por quais número ele é divisível.
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