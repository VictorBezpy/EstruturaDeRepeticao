#32.py
"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""
n = int(input('Digite um número para fatorar:'))
print('%d! = ' %n, end = " ")
i = 1
fat = 1
while i <= n:
	print(i, '.', end = " ")
	fat *= i
	i += 1
print('= %d' %fat, end = " ")