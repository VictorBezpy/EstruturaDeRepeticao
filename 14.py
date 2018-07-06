#14-parimp.py
"""
14. Faça um programa que peça 10 números inteiros, calcule e mostre a 
quantidade de números pares e a quantidade de números impares.
"""
vetor = []
i = 1
par = 0
imp = 0
while i <= 10:
	n = int(input('Digite um número: '))
	vetor.append(n)
	i += 1
	if n % 2 == 0:
		par += 1
	else:
		imp += 1
print('Você digitou %d números pares e %d números impares.' %(par, imp))