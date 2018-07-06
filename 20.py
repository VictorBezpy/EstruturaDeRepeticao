#20-fat2.py
"""
20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o
fatorial várias vezes e limitando o fatorial a números inteiros positivos e 
menores que 16.
"""
while 1 == 1:
	n = int(input('Digite um número para fatorar:'))
	while n < 0 or n > 16:
		n = int(input("Valor não aceito, digite um número: "))
	else:
		i = n
		fat = 1
		while i > 1:
			fat *= i
			i -= 1
	print('Fat(%d) = %d' %(n, fat)) 
