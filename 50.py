#50.py
"""
50.Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o 
valor de H com N termos.
"""
x = int(input('Digite o limitador: '))
n = 1
m = 1
soma = 0
print('H =', end=' ')
while m <= x:
	print(n, '/' m, '+' , end=' ')
	soma = soma + (n / m)
	m += 1

print('=', soma)