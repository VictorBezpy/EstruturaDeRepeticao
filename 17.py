#17-fat.py
"""
17. Faça um programa que calcule o fatorial de um número inteiro fornecido 
pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""
n = int(input('Digite um número para fatorar:'))
i = 1
fat = 1
while i <= n:
	fat *= i
	i += 1
print('Fat(%d) = %d' %(n, fat))